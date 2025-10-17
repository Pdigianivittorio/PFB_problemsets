#!/usr/bin/env python3 

#write a script in which you construct a dictionary of your favorite things: 
my_fav_dic = {'book' : 'Jitterbug' , 
                 'song' : 'Tom Petty',
                 'tree' : 'Cedar'}
print(f"My dictionary is: {my_fav_dic}")

#now I want to print out my favorite book 
print(f"my favorite book is {my_fav_dic ['book']}")

#now I want to print out my favorite book using a variable in the key
my_fav_thing = 'book'
print(f"my favorite book is {my_fav_dic [my_fav_thing]}")

#now I want to print my favorite tree, I will try using the key in the dictionary and also making its own variable. 
print(f"my favorite tree is {my_fav_dic ['tree']}")

my_fav_tree = 'tree'
print(f"my favorite tree is {my_fav_dic [my_fav_tree]}")

# Now I want to update my dictionary to include my favorite organism (key) and value 
my_fav_dic.update({'organism' : 'bacteria'})
print(f"my new and updated dictionary is: {my_fav_dic}")

#now I want to print the key and value of my new/updated dictionary using a for loop
for key in my_fav_dic:
        favs = my_fav_dic[key]
        print(key, favs)
    
    



