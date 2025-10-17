#!/usr/bin/env python3

import re


#nt_ct = {"geneIDa" : {"A" : 2 , "G" : "4" , "C" : "6" , "G" : "2"} , "geneIDb" : {"A" : "2" , "G" : "4" , "C" : "6" , "G" : "2"} , 
        # "geneIDc" : {"A" : "2" , "G" : "4" , "C" : "6" , "G" : "2"}}

#print(nt_ct ["geneIDa"]["A"])


seq_ct_dict = {}
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

            #this is initializing a dictionary for nucleotide counts
            nt_count = {"A" : 0 , "T" : 0 , "G" :0 , "C" : 0}
            seq_ct_dict[geneID] = nt_count
            #adds the nucleotide count dictionary to seq_ct_dict under the current geneID
           
        else: #this line runs if the line is NOT A HEADER, meaning its a sequence line
            seq_ct_dict[current_gene]["A"] += line.count("A")
            seq_ct_dict[current_gene]["T"] += line.count("T")
            seq_ct_dict[current_gene]["G"] += line.count("G")
            seq_ct_dict[current_gene]["C"] += line.count("C")
            #counts the number of A.T,G,C characters in the current line and adds them to the total for the cuurent_gene
            
for geneID, counts in seq_ct_dict.items():
    print(f"{geneID} : A = {counts["A"]} T = {counts["T"]} G = {counts["G"]} C = {counts["C"]}")

#writing and output to a new file 
output_path = "/Users/pfb/PFB_problemsets/python8/nucleotide_counts_ProblemSet8_1.txt"
#sets the path where the ouput file should be saved 
with open (output_path, "w") as out_file:
    #opens the ouput file in write mode ("w", meaning it will create a new file or overwrite an existing one)
    for geneID, counts in seq_ct_dict.items():
    #loops for each gene and its nucleotide counts in the seq_ct_dict
        out_file.write(f"{geneID} : A = {counts["A"]} T = {counts["T"]} G = {counts["G"]} C = {counts["C"]}")
        #writes a formatted line to the output file for each gene, showing counts of A, T, G, C

print(f"Output written to {output_path}")
#prints a message in the terminal to let the user know where the ouput was saved. 
            
           
           
           
           
           