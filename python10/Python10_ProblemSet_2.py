#!usr/bin/env python3

dna ='''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

#ideally we want to create a function to split the nucleotide string into 60 nt segments 
def format_dna(dna):
    #this defines a function named "format_dna" that takes a single argument "dna"
    #(dna) = important becuase the function expects a string (a DNA sequence) as input 
    clean_dna = dna.replace ('\n' , '')
    #this creates a new variable to replace DNA in which the \n (new line character) is replaced with '' no space
    #this ensures that you are working with one continuous string- allowing for clean formatting later    
    formatted = '' # initializes an empty string called "formatted"
    #this will store the final results as the DNA is broken into 60-character lines 
    for i in range(0 , len(clean_dna), 60):
        # starts a loop that goes from i = 0 to the end of the DNA string, in steps of 60 
        #the purpose here is to divide the DNA into chunks of 60 characters 
        formatted+=clean_dna[i:i+60] + '\n'
        # you can also write this as: formatted = formatted + (clean_dna[i:i+60] + '\n')
        # this takes a 60 character slice from the string and adds it to formatted, followed by a new line character 
    
    return formatted
    # formatted is now a nicely formatted string 

formatted_dna = format_dna(dna)
print(formatted_dna)


