#!/usr/bin/env python3


#purpose: 1). parse through a FASTA file, 2). count nucleotide composition per sequence, 3).break each sequence into codons (in 1st reading frame), 
#4). and write both the codon lists and nucleotide counts to an ouput file. 
import re # imports regular expressions module for pattern matching 

seq_dict = {}
#this will be the dictionary that will store nucleotide counts for each gene 
    #format  {geneID : {"A" : count , "T" : count , "G" : count , "C" : count}}
current_gene = None
#a variable to track the current geneID while reading the file 

with open("/Users/pfb/PFB_problemsets/python8/Python_08.fasta.txt" , "r") as seq_file_object:
    #open the input FASTA file in read mode "r"
    #seq_file_object is a file object used to iterate through lines in the file
    for line in seq_file_object:
        #establishing a foor loop to go over each line in the input file
        line = line.rstrip ()

        
        if line.startswith('>'):
            #checks if the line in the FASTA header (starts with >). These lines contain the sequence ID. 
            found = re.search(r">(\S+).+", line)
            #used a regular expression to extract the geneID
                #\S+ matches the string of non-whitespace characters after the > symbol
            geneID = found.group(1)
                #saves the matched gene ID (the first group [1] from the regular expression), into the variable geneID
            current_gene = geneID
                #sets current_gene so we can associate the upcoming nucleotide lines with the correct geneID. 
            seq_dict[geneID] = " "

        else: 
            seq_dict[current_gene] += line.upper() #add sequence, make uppercase for consistency 

#Processing each sequence into condons 
output_path = '/Users/pfb/PFBproblemsets/python8/codon_output.txt'

#Print to the screen before writing the file 
print("\nCODONS (first reading frame):\n" + " "*35)
for geneID, full_seq in seq_dict.items():
    codons = [full_seq[i:i+3] for i in range(0, len(full_seq) - 2, 3)]
    print(f"{geneID}:")
    print(" ".join(codons) + "\n")

#write to file: 
with open("codon_output", "w") as out_file:
    #"codon_output" needs to be in quotes because if there is no quotes, python thinks there is a variable with that name instead of treating it as a filename.
    for geneID, full_seq in seq_dict.items():
        codons = [full_seq[i:i+3] for i in range(0, len(full_seq) - 2, 3)]
        out_file.write(f"{geneID}:\n")
        out_file.write(" ".join(codons) + "\n\n")

print(f"Codon output written to: {output_path}")

########## the script results in an error 


           
           
           
           
           