#!/usr/bin/env python3

import argparse
from collections import Counter, defaultdict
import math

def shannon_entropy(seq):
    """Calculate Shannon entropy of a sequence."""
    length = len(seq)
    freqs = Counter(seq)
    entropy = 0
    for base in freqs:
        p = freqs[base] / length
        entropy -= p * math.log2(p)
    return entropy

def count_kmers(fastq_file, k):
    counts = Counter()
    with open(fastq_file, 'r') as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num % 4 == 2:
                seq = line.strip()
                for i in range(len(seq) - k + 1):
                    kmer = seq[i:i+k]
                    counts[kmer] += 1
    return counts

def build_kmer_graph(kmer_counts):
    """Build graph mapping each kmer to possible next kmers overlapping by k-1 bases."""
    graph = defaultdict(list)
    k = len(next(iter(kmer_counts)))  # infer k from any kmer

    prefix_map = defaultdict(list)
    for kmer in kmer_counts:
        prefix = kmer[:-1]
        prefix_map[prefix].append(kmer)

    for kmer in kmer_counts:
        suffix = kmer[1:]
        graph[kmer] = prefix_map.get(suffix, [])
    return graph

def extend_contig(seed, graph, kmer_counts):
    """Extend contig forward from seed by choosing highest count next kmer."""
    contig = seed
    current = seed
    k = len(seed)

    visited = set([seed])
    while True:
        next_kmers = graph.get(current, [])
        if not next_kmers:
            break
        # Pick next kmer with highest count
        next_kmer = max(next_kmers, key=lambda x: kmer_counts[x])
        if next_kmer in visited:
            break  # avoid cycles
        contig += next_kmer[-1]
        current = next_kmer
        visited.add(next_kmer)

    return contig

def assemble_contigs(kmer_counts, min_entropy=1.5, top_seeds=10):
    seeds = [kmer for kmer in kmer_counts if shannon_entropy(kmer) >= min_entropy]
    seeds = sorted(seeds, key=lambda x: kmer_counts[x], reverse=True)[:top_seeds]

    graph = build_kmer_graph(kmer_counts)
    assembled_contigs = []

    for seed in seeds:
        contig = extend_contig(seed, graph, kmer_counts)
        assembled_contigs.append((contig, kmer_counts[seed]))

    return assembled_contigs

def main():
    parser = argparse.ArgumentParser(description="Count kmers and assemble contigs from FASTQ reads.")
    parser.add_argument("fastq_file", help="Input FASTQ file")
    parser.add_argument("k", type=int, help="K-mer size")
    parser.add_argument("--top", type=int, default=10, help="Number of top seeds to assemble")
    parser.add_argument("--min_entropy", type=float, default=1.5, help="Minimum entropy for seed kmer")
    args = parser.parse_args()

    print(f"Counting {args.k}-mers in {args.fastq_file}...")
    kmer_counts = count_kmers(args.fastq_file, args.k)

    print(f"Assembling contigs from top {args.top} seeds with entropy >= {args.min_entropy}...")
    assembled_contigs = assemble_contigs(kmer_counts, min_entropy=args.min_entropy, top_seeds=args.top)

    print("\nAssembled contigs:")
    for i, (contig, count) in enumerate(assembled_contigs, 1):
        print(f">contig_{i} count={count}")
        print(contig)

if __name__ == "__main__":
    main()
