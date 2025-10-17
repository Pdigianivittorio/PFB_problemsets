#!/usr/bin/env python3

count = 0
sum = 0
while count < 101:
    #here, i chose to do <101 becuase I wanted to include 100 in my analysis 
    #YOU CAN TO THE < 100, this will give you all the count from 0 to 99, however. If you do this option you do not have to the count -1 option below
    #becuase you are including the sum of every number between 1 and 100 (but not including 100?)
    print (f"count: {count}")
    count+=1
    sum = sum + count-1
    #here, i did the sum count -1 because I didn't want the sum to include 101 in the sum total, just number 1-100 
print ("Done")
print (f"the sum is {sum}")


#another script culd be: 
# count = 0
# sum = 0 
# while count < 100: 
#   print(f"count: {count}")
#   count+=1
#   sum = sum + count 

