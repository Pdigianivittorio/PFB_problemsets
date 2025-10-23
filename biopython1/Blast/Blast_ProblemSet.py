#!/usr/bin/env python3

from Bio import SeqIO

fasta_file = "/Users/pfb/PFB_problemsets/biopython1/Blast/uniprot_sprot.fasta"
for record in SeqIO.parse(fasta_file, "fasta"):
    print("ID %s" % record.id)
    print("Sequence length %i" % len(record))
    print( "Sequence Description %s" % record.description)