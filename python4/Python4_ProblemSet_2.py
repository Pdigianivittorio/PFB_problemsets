#!/usr/bin/env python3

taxa_string = "sapiens : erectus : neanderthalensis"
print(taxa_string)

#splitting taxa_string into a list called taxa_list. Using " : " as the seperator 

taxa_string.split(":")
taxa_list = taxa_string.split(":")
print(taxa_list) 
print(f"index placement 1 is {taxa_list[1]}")

#this is to identify the types of string and list 
print(type(taxa_string))
# output of this = <class 'str'>
print (type(taxa_list))
# output of this = <class 'list'>

# now I want to sort the taxa_list alphabetically 
taxa_list.sort()
print(f"the alpabetical sorting of taxa_list is {taxa_list}")

#n now I want to sort the taxa_list by the length of the list
taxa_list.sort(key = len)
print (f"the sorting of the taxa_list by length of the string is {taxa_list}")

