#!/usr/bin/env python3

import sys

def read_fasta(filename):
    #reads a FASTA file and return the sequence as a single string 
    sequence = ''
    # initializes and empty list for sequence 
    with open (filename, 'r') as file: 
        for line in file: 
            if not line.startswith('>'): #this allows you to ignore header lines 
                sequence += line.strip()
    return sequence

def format_dna(dna, width): #formats the DNA sequence into lines of given width.
    lines = [] # here you are going to make a list of strings equal to the number of nts you are parsing out. 
    for i in range(0, len(dna), width):
        lines.append(dna[i:i+width])
    return '\n'.join(lines)

fasta_file = sys.argv[1]
line_width = int(sys.argv[2])

dna_sequence = read_fasta(fasta_file)
formatted_sequence = format_dna(dna_sequence, line_width)
print (formatted_sequence)
