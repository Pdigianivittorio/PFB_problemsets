#!/usr/bin/env python3 

# create a new empty dictionary: this will allow yout to stoe nucelotide count with nucleotide letters (A,T,C,G) as keys and their counts as values. 
nt_count = {}

# 1st- set the varible which is the DNA sequence 
dna = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'
print (f"this is the original sequence: {dna}")

#create a set (since the set will allow for unique characters to be chosen within the DNA sequence)
#using set(dna) unsures each nucleotide is counted only once.
unique_nt = set(dna)
print (f"unique nt: {unique_nt}")

#iterate through each unique nucleotide 
for nt in unique_nt:
    #count the number of this unique nucleotide in the original DNA sequence 
    count = dna.count (nt)
    #.count(nt) gives the total occurences of each nucleotide in the sequence 

    # add count to dictionary; stores results into dictionary 
    nt_count[nt] = count

print ('nt count:', nt_count)

#store each nucleotide in a dictionary 
for nt in sorted (nt_count.keys()):
        #this loops through the nucleotide keys in sorted order- alphabetically 
    print (f"{nt}:{nt_count[nt]}")

#now I wan to calculate the GC content of the DNA sequence 
g_nuc = dna.count('G')
c_nuc = dna.count('C')
full_length_dna = len(dna)
GC_content = (g_nuc + c_nuc)
print (f"the GC content of the dna sequence is {GC_content/full_length_dna:.2%}")

