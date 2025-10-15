#!/usr/bin/env python3
import sys

# create a variable that stores a string that represents a DNA sequence

dna = sys.argv[1]

# remember when you define a variable in a script, and it is not an integer, it has to be in quotes! 

# make all nucleotides in DNA sequence lower case 

dna_lowercase = dna.lower () 
print(dna_lowercase)

# now, I want to count the # of a's in the DNA sequences 
# it is easiest to redefine variables so that you can print easier, I made these variables random letters for ease, especially since I can use this script later

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

#now I want to replace all T's with U's in the nucleotide sequence 
b = dna_lowercase.replace ('t', 'u')
print (f" RNA sequence is as follows : {dna_lowercase.replace ('t', 'u')}")

#now I want to calculate the CG content % in DNA 
c = len(dna_lowercase)
dna_GC_count = (z + a)
print (f"the GC content of the DNA sequence is {dna_GC_count/c:.2%}")

# subsequently I want to calculate the AT content % of the DNA sequence 
c = len(dna_lowercase)
dna_AT_count = (x + y)
print (f"the AT content of the DNA sequence is {dna_AT_count/c:.2%}")



 