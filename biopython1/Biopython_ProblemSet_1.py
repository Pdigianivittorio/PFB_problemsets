#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import re

fasta_file = "/Users/pfb/PFB_problemsets/biopython1/sequences.nt.fa"

sequences = list(SeqIO.parse("/Users/pfb/PFB_problemsets/biopython1/sequences.nt.fa" , "fasta"))

sequences.sort(key = lambda seq_record : len(seq_record.seq)) #uses lambda to sort from shortest to longest sequence 
#if you want longest to shortest, use: reverse=True


#in the below block of code, the goal is to simply use Biopython functions to print the sequence name, description, and sequence 
for seq_record in sequences:
    #SeqIO.parse() = reads the .fasta (.fa) file and parses it. The format "fasta" tells it to look for FASTA files specifically. 
    seq_str = str(seq_record.seq).upper()#This line converts the sequence (seq_record.seq) to a plain string (instead of a sequence object) 
                                        #I think it is good practice to always convert case of sequences to upper case. 
    nucleotide_counts = {'A' :0 , 'T' :0 , 'G' : 0 , 'C' : 0} #initializing manueal nucleotide count dictionary with each nucleotide key set to 0
                                                            # this will be used to manually count each base 


    #now I want to count each nucleotide manually, but making sure we are still in the SeqIO loop. 
    for base in seq_str: # this loops every base into the sequence string
        if base in nucleotide_counts: #checks if the base is one of the 4 expected nucleotides
             nucleotide_counts[base] +=1 #if there is one of our expected nucleotides, you increase the count of the nucelotide by 1. 
        #else: don't need an else statement

    #print sequence details 
    print('ID' , seq_record.id , "\t")
    print('Sequence', seq_record.seq , "\t")
    print('Length' , len(seq_record) , "\t")
    print("Nucleotide counts:")
    for nucleotide in ["A" ,"T" , "C" ,"G"]: #loops through the expected bases and prints their individual counts
                                            # accesses each count from the nucleotide_counts directory 
            print (f"{nucleotide} : {nucleotide_counts[nucleotide]}")
   
    #with open (fasta_file, "r") as GC_count: 
    #for seq_record in SeqIO.parse (GC_count, "fasta"):
    gc_percentage = gc_fraction(seq_record.seq) *100
    print(f"GC content:{gc_percentage:.2f}%")
    

    #print() #blank line between
        #for better readibility 

     

#in the block of code below, the goal is to use Biopython to print out stats about my FASTA file. 
def count_sequences(fasta_file): # this line defines a function named count_sequences that take one argument:fasta_file. This argument will be the path to the FASTA file you want to count sequence in. 
    # the count_sequences function will contain the information needed to count the number of sequences in the provided FASTA file. 
    count = 0 #initializing count = 0 (basically starting count at 0)
    for record in SeqIO.parse("/Users/pfb/PFB_problemsets/biopython1/sequences.nt.fa" , "fasta"): #for loop that iterates over each SeqRecord object parse in the FASTA file
        count +=1 # for each sequence, we increment the count by 1. 
    return count #after the loop finishes, the count holds the total number of sequences, which is then returned
total_sequences = count_sequences(fasta_file)
print(f"Total number of sequences : {total_sequences}")



    