#!usr/bin/env python3

#below is a script that makes my function have two arguments: 1- showcasing the DNA se, 2-setting the width of segments of how many nts you want ti display 

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# the problem set told me the length of the string of nts was 80 

#ideally we want to create a function to split the nucleotide string into 60 nt segments 
def format_dna(dna, x):
    #here x is some number signifying some nt length I want per line 
    lines = [] # starting with an empty list to hold chunks 
    for i in range(0 , len(dna), x): #go from 0 to the end of the string, in steps of 60 
        chunk = dna[i:i+x] #get a 60 character slice of the DNA
        lines.append(chunk) #add that chunk to the list 
    return '\n'.join(lines) #join the chunks with newlines and return 
    
  
formatted_dna = format_dna(dna, 80)
#here in the second paramter, I have the nucleotide size I want.  
print(formatted_dna)