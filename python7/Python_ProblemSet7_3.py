#!/usr/bin/env python3

import re
#to use the reglar expression function to allow your script to be ran, you must use the import re

seq_file = open("Python_07.fasta.txt" , "r")
for line in seq_file: 
    line = line.rstrip()
    print(line)
    pattern = r"^\>\w+"
    len(re.findall(pattern,line))
    print(f"this line has {len(re.findall(pattern,line))} match to my pattern")

pattern_match = seq_file.read()
pattern = r"^\>\w+"
len(re.findall(pattern,pattern_match))
print(f"file: {pattern_match}")
#print(f"this file has {len(re.findall(pattern,pattern_match))} matches to my pattern")