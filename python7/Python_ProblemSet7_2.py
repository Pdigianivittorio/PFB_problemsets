#!/usr/bin/env

import re 
 #to use the reglar expression function to allow your script to be ran, you must use the import re

with open("Python_07_nobody.txt" , "r") as poetry_file_object, open("Pauline.txt" , "w") as poetry_file_object_write:
    for line in poetry_file_object:  
        phrase = line        
        new_phrase = re.sub(r'Nobody' , 'Pauline', phrase)
        print(new_phrase)
        poetry_file_object_write.write (new_phrase)