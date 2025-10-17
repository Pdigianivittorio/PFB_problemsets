#!/usr/bin/env python3

with open("/Users/pfb/PFB_problemsets/python6/Python_06.fastq.txt" , "r") as fastq_object:
    count_line = 0
    seqID = 0
    nt_seq = 0
    for line in fastq_object:
        count_line += 1
        line = line.rstrip()
        len(line) 
        print(f"this line number is {count_line}")
        print(f"This line is this many characters long: {len(line)}")

        if count_line % 4 == 1:
            # the idea here is that I can count every 4th line, starting at 0 is a seqID 
            seqID += 1
            print(f"Found seqID # {seqID}")
        if count_line % 4 == 2:
            print(line)
            #the idea here is that I can count every 2nd lines in a 4-line block (this is the nucleotide seq)
            nt_seq += 1
            len(line)
            print(f"this is the length of the nucleotide sequence on this line: {len(line)}")
print (f"total number of seqIDs: {seqID}")