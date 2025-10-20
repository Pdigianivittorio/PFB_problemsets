#!/usr/bin/env python3

from Bio import SeqIO
for seq_record in SeqIO.parse("/Users/pfb/PFB_problemsets/biopython1/sequences.nt.fa" , "fasta"):
    print('ID' , seq_record.id , "\t")
    print('Sequence', seq_record.seq , "\t")
    print('Length' , len(seq_record) , "\t")
   
