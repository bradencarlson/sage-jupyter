#!/usr/bin/env python
# coding: utf-8

# # Dictionaries
# 
# In this document, we discuss dictionaries.  Dictionaries are a powerful data structure in Python that are similar to 
# lists.  While lists contain an array of items, that can be accessed via their index, dictionaries contain key-value
# pairs.  Much like real dictionaries, Python dictionaries keep track of a certain number of items, as well as their 
# values in a single structure.  We demonstrate this in the following example.

# In[ ]:


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(my_dict['a'])


# In this example, we define a dictionary that has five keys: $a,b,c,d$ and $e$.  Whose values are $1,2,3,4$ and $5$ 
# respectively.  We then print out the value that corresponds to the key $a$.  Dictionaries are often used for counting
# objects, we do this in the following example:

# In[ ]:


counts = {}

string = "Here is some string of information that we will use for counting.  We will count the number of each letter that appears in this string."

for letter in string:
    if letter in counts.keys():
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1

print(counts['a'])


# This will prove a very useful feature of Python, especially when we talk about frequency analysis when tring to crack 
# a shift cipher without the use of brute force.  
# 
# It is also interesting to note that the keys and values can be pretty much whatever we need them to be.  We 
# demonstrate this in the next example.

# In[ ]:


my_dict = {'b': "This is a list", 
           "string": "This is a string", 
           14: ["nothing", 45, 9209],
           23.4: "This is a decimal"}

print(f"The value of my_dict[14] is: {my_dict[14]}")


# A note about this, the way that all of this information is stored in the computer, the computer computes the 
# hash of the key.  We do not need to know to much about this execpt for the fact that any hashable object may be 
# used as a key.  Hashable types include:
# 
# * int's
# * str (string)
# * decimal numbers
# * Groups inherited from SageMath
# * tuples
# * and others
# 
# Unhashable types include 
# 
# * lists
# * dictionaries
# * and others
# 
# Thus we cannot use these types as keys in our dictionaries.  We can also use iteration to access all the elements
# in a dictionary just like we did with lists.  There are a few differences to this though; dictionaries offer a
# few different ways of accessing their elements:
# 
# * The `.keys()` method, which retuns a list of all the key values in the dictionary
# * The `.values()` method, which returns a list of all the values in the dictionary
# * The `.items()` method, which returns a list of tuples containing each key-value pair in the dictionary.  
# 
# We demonstrate all three of these in the example that follows.

# In[ ]:


my_dict = {}

x = [i^3 for i in range(0,15)]
y = [i for i in range(0,15)]

for i in range(0,len(y)):
    my_dict[f"{i}^3"] = x[i]

print(my_dict)


# In[ ]:


for k in my_dict.keys():
    print(k)
for v in my_dict.values():
    print(v)


# One note about using the `.items()` method.  We will use this most when we wish to access both the key and its 
# value for every element in the dictionary.  In doing so, since this method returns a list of tuples, we need 
# not one but two iterators to accomplish this.  We show how this is done in the following example:

# In[ ]:


for k,v in my_dict.items():
    print(f"The value of {k} is {v}")


# We will use dictionaries quite a bit throughout this project, so practice using these as we will use them 
# in the future to count cosets, conjugacy classes, and more.
