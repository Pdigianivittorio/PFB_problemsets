#!/usr/bin/env python3

#writing a script to generate and print the reverse compliment 

#first I want to define the variable: 

dna_sequence = "GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT"
print(f"this is the original DNA sequence: {dna_sequence}")

dna_upper = dna_sequence.upper ()
print(f"this is the uppercase original DNA sequence: {dna_upper}")

reverse_sequence = dna_upper[::-1]
print(f"this is the reverse of the original uppercase sequence: {reverse_sequence}")

rev_complement_sequence = []
#in this case it is important to start with an empty list 
for base in reverse_sequence:
    if base == 'A':
        rev_complement_sequence.append ('T')
    elif base == 'T':
        rev_complement_sequence.append ('A')
    elif base == 'C':
        rev_complement_sequence.append ('G')
    elif base == 'G':
        rev_complement_sequence.append ('C')
    #else: 
        #rev_complement_sequence.append(base)
        #you don't need an else sequence 

#if you run this as is, it will spit out a string of nucleotides in a list, not in sequence format. Thus, you will have to join them together into 1 string

rev_complement_sequence = ''.join(rev_complement_sequence)
#here we can redefine what rev_complement_sequence is , it will be the joined version of all the strings of nucleotides that was the ouput of 
#the else/if arguments 

print(f"this is the reverse complement sequence: {rev_complement_sequence}")

#Now, I want to find at a specific spot where the EcoRI restriction site is in the sequence (but in the original uppercase sequence): 
restriction_site_upp = dna_upper.find('GAATTC')+1
# when converting from index to position +1 
print(restriction_site_upp)

restriction_site_low = dna_upper.find('GAATTC')+6
print(restriction_site_low)

