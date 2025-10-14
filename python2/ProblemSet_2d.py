#!/usr/bin/env python
import sys

# creating nested tests 
# here I created nested nests per each argument that may be true (since python will stop running when it comes across something new)
# It is helpful to go about ordering by level of priority (going to the point above) 

count = int(sys.argv[1])
# here I made this script where I can test numbers on the command line
#to do this, I used sys.argv so I can list the number I want to test on the command line. 
#then, in order to actually test numbers using this system, I had to delineate the sys.argv as an integer (so I can make this string a number)
if count < 0: 
    print (count, "is negative")
    if count % 2 == 0:
        print (count, "is even")
    else:
        print (count, "is odd")
    if count % 3 == 0:
        print (count, "is divisible by 3")
    else:
        print (count, "is not divisible by 3")
elif count > 0:
    print (count, "is positive")
    if count < 50:
        print (count, "is less than 50" ) 
    if count > 50:
        print (count, "is over 50")
    if count % 2 == 0:
        print (count, "is even")
    else:
        print (count, "is odd")
    if count % 3 == 0:
        print (count, "is divisible by 3")
    else:
        print (count, "is not divisible by 3")
        
else: 
    print (count, 'is equal to 0')


# In this example, I used elif count > 0: as oppossed to else. This is becuase elif helps in specifying a value before the colon. 
# In an instance where you have a few elif statements, you follow with else (as the last statement doesn't need to have specificity)