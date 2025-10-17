#!/usr/bin/env python3

import re
#to use the reglar expression function to allow your script to be ran, you must use the import re

pattern = r"^\>\w+"

seq_file = open("Python_07.fasta.txt" , "r")
print(seq_file)