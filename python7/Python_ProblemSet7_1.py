#!/us/bin/env python3 

import re 
 #to use the reglar expression function to allow your script to be ran, you must use the import re

poetry_file_obj = open("Python_07_nobody.txt" , "r")
for line in poetry_file_obj: 
    print(line)
    # I chose to print line so that I can follow easier 
    found = re.findall(r"Nobody" ,line)
    print(f"this line has: {found}")
    # This is to find in each line if there is "Nobody"

    #the below for loop, is to find the start and end position of Nobody in each line 
    for match in re.finditer(r"Nobody", line):
        whole = match.group (0)
        whole_start = match.start(0) + 1
        whole_end = match.end(0)
        print(whole , whole_start, whole_end)