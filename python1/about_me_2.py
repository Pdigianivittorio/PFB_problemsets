#!/usr/bin/env python3
import sys

#this is also another way to generate list where you would define the variables on the command lin
#to do this you would use sys.argv [1] etc, here and then define the variable in the command line 
#When completing lists in this way, it is important to write import sys in the line under the #!usr/bin/env python3

name = sys.argv [1]
print ("my name:", name)

favorite_color = sys.argv [2]
print ("my favorite color:", favorite_color)

favorite_activity = sys.argv [3]
print ("my favorite activity:", favorite_activity)

favorite_animal = sys.argv [4]
print ("my favorite animal:", favorite_animal)


