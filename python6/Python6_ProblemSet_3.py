#!/usr/bin/env python3


file_object = open("/Users/pfb/PFB_problemsets/python6/Python_06.seq.txt" , "r")
# in this text file the format of the file exists as: seqname\tsequence\n ; where \t=tabe from seq name to sequence and \n=new line 
for line in file_object:
    cleaned_line = line.rstrip('\n')
    my_list = cleaned_line.split("\t")
    # to make accessing the sequence specifically. you can split the column and sequence into individual strings, so that you can later access the sequence by using [1]
    print(f"this is the original sequence \n{my_list [0]} \n{my_list [1]}")
    #Now I want to create the reverse sequence of each line, by defining a new variable and reversing that sequence
    seq = my_list[1]
    print (f"this is the reverse sequence \n{my_list [0]} \n{seq [::-1]}")

    reversed_seq = seq[::-1]

    reversed_comp_seq = []
    for base in seq[::-1]:
        if base == 'A':
            reversed_comp_seq.append ('T')
        elif base == 'T':
            reversed_comp_seq.append ('A')
        elif base == 'C':
            reversed_comp_seq.append ('G')
        elif base == 'G':  
            reversed_comp_seq.append ('C')
    
    rev_complement_sequence = ''.join(reversed_comp_seq)

    print(f"this is the reverse complement sequence: \n{my_list [0]} \n{rev_complement_sequence}")
  

    