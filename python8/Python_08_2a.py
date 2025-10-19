#!/usr/bin/env python3


#purpose: 1). parse through a FASTA file, 2).count nucleotides per sequence. 3). break each sequence into codons (in 1st reading frame), 
#4). and write both the codon lists and nucleotide counts to an ouput file. 

import re # imports regular expressions module for pattern matching 

seq_ct_dict = {}
# Initialize an empty dictionary to store nucelotide counts per gene 

codon_dict = {}
#Initializing an empty dictionary to store codon lists pere gene 

with open("/Users/pfb/PFB_problemsets/python8/Python_08.fasta.txt" , "r") as seq_file_object:
    #open the input FASTA file in read mode "r"
    #seq_file_object is a file object used to iterate through lines in the file
    for line in seq_file_object: #loops through each line of the FASTA file 
        line = line.rstrip () #removes any trailing whitespace (like newline characters)

        
        if line.startswith('>'): #identifies the header line of a new gene sequence (starting here with the geneID)
            found = re.search(r">(\S+).+", line) # extracts the sequence/gene ID (non-whitespace characters after >)
            geneID = found.group(1)
        
            nt_count = {"A" :0 , "T" : 0 , "G" : 0 , "C" : 0}
            seq_ct_dict[geneID] = nt_count #stores this is the main directory 
            #here, the seq_ct_dict is the master dictionary. nt_count is a subdictionary in the seq_ct_dict
            #thus if you print the seq_ct_dict[geneID], in return you will key the nt_count as you are using this dictionary as the value of the seq_ct_dict

            seq = " " #initializes an empty string to build the full DNA sequence 


        else: 
            #counts nucleotides in this line and updates the nt_count dictionary as corresponding values 
            nt_count["A"] += line.count("A")
            nt_count["T"] += line.count("T")
            nt_count["G"] += line.count("G")
            nt_count["C"] += line.count("C")

            seq += line #appends the line to the sequence string 

            #after appending sequence, we need to update the codons for the codon_dict 
            codons = [seq[i:i+3] for i in range(0, len(seq)-2, 3)] #this breaks sequence into codons (frame 1)
            codon_dict[geneID] = codons #now storing codons in the diciontary 

#print output to screen before writing to file
print("GeneID\tA\tT\tC\tCodons")
for gene in seq_ct_dict: 
    print(f" GeneID: {gene}, 
          A: {seq_ct_dict[gene]["A"],}
          T: {seq_ct_dict[gene]["T"],} 
          G: {seq_ct_dict[geneID]["G"],}
          C: {seq_ct_dict[geneID]["C"],}
          codon_dict[gene], sep = "\t")

#writing results to a new output file 
with open ("codon_output_2.txt" , "w") as out_file: 
    out_file.write(f" GeneID: {"GeneID"}\t A: {"A"}\t T:{"T"}\t G:{"G"}\t C:{"C"}\tCodons\n") #writing a header row in the output file 

    for gene in seq_ct_dict: #loop through each geneID
        #writing each gene and its nucleotide counts and codon list to file 
        out_file.write(f"GeneID:{gene}\t A:{seq_ct_dict[gene]['A']}\t T:{seq_ct_dict[gene]['T']}\t G:{seq_ct_dict[gene]['G']}\t C:{seq_ct_dict[gene]['C']}\t{' , '.join(codon_dict[gene])}\n")

           
           
           
           
           