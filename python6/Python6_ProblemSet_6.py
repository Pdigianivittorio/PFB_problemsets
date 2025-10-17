#!/usr/bin/env python3


# below is the script for reading a file and writing a new file. 
with open ("/Users/pfb/PFB_problemsets/python6/Python_06.txt" , "r") as file_read, open ("/Users/pfb/PFB_problemsets/python6/Python_06_uc.txt" , "w") as file_write:
    for line in file_read:
        line = line.upper() 
        file_write.write (line)
    file_write.write("\n")
