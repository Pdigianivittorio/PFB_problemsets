#!/usr/bin/env python
import sys

# creating nested tests 
# here I created nested nests per each argument that may be true (since python will stop running when it comes across something new)
# It is helpful to go about ordering by level of priority (going to the point above) 

count = 27
# Here, I can put a numnber after the count = and run the script using 
    # python3 ProblemSet_2c.py 
    # it will give me the results of the test when I wanted to test the number 27. 
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