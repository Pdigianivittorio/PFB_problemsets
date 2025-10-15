#!/usr/bin/env python3
import sys

# create a variable that stores a string that represents a DNA sequence

dna = sys.argv[1]

# remember when you define a variable in a script, and it is not an integer, it has to be in quotes! 

# make all nucleotides in DNA sequence lower case 

dna_lowercase = dna.lower () 
print(dna_lowercase)

# now, I want to count the # of a's in the DNA sequences 
# it is easiest to redefine variables so that you can print easier
x = dna_lowercase.count('a')
print (f"there are {dna_lowercase.count ('a')} nucleotide a's")

y = dna_lowercase.count ('t')
print (f"there are {dna_lowercase.count ('t')} nucleotide t's")

z = dna_lowercase.count ('c')
print (f"there are {dna_lowercase.count ('c')} nucleotide c's")

a = dna_lowercase.count ('g')
print (f"there are {dna_lowercase.count ('g')} nucleotide g's")

#since this script allows you to put any sequence in the command line to test, you can use a positive control on the command line and test the script with a short nucleotide seq: GATCG

#to use this script on the command line with any other DNA sequence: 
# python3 Python3_ProblemSet_b.py <other DNA seq>

