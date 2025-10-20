#!/usr/bin/env python3


dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

#ideally we want to create a function to split the nucleotide string into 60 nt segments 
def format_length(dna):
    #this defines a function named "format_dna" that takes a single argument "dna"
    #here, dna is expected to be a string made up nucleotide characters with NO line breaks

    #this line splits the longDNA string into substrings of 60 characters using a list comprehension (which is a for loop in a list )
    lines = [] # starting with an empty list to hold chunks 
    for i in range(0 , len(dna), 60): #go from 0 to the end of the string, in steps of 60 
        chunk = dna[i:i+60] #get a 60 character slice of the DNA
        lines.append(chunk) #add that chunk to the list 
    return '\n'.join(lines) #join the chunks with newlines and return 
    
  
formatted_dna = format_length(dna) 
print(formatted_dna)