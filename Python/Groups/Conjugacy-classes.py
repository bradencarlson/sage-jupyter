#!/usr/bin/env python
# coding: utf-8

# # Conjugacy Classes

# Here we discuss conjugacy classes.  Given some element $g$ in a group $G$.  We can calculate the conjugate of $g$ 
# with respect to some other element $x\in G$, by calculating the following
# $$ ^gx = xgx^{-1}  $$
# The set of all conjugates of $g$ in $G$, is denoted by $^Gg$, and is called a conjugacy class.  We implement code
# in this file to calculate the conjugacy classes of a group.

# In[ ]:


# define the conjugacy_class function.  This function will take in an element
# as well as a group, then will calculate the conjugacy class of that element in the 
# group given.  See below for an example.
def conjugacy_class(element , group):
    # define a set to hold all the conjugates of the element
    conjugates = set(())
    # for each item in the group, calculate the conjugate and add
    # it to the set defined in the line above.
    for i in group.list():
        conjugates.add((i^(-1))*element*i)
    # return the final set of all conjugates of the element.
    return conjugates


# Here we go through our first example.  We define the set $S_5$, and we define $\sigma$ to be $(123)\in S_5$.  We 
# then use our newly defined function to calculate the conjugacy class of $\sigma$ in $S_5$.

# In[ ]:


# define the group S5
S5 = SymmetricGroup(5)

# define sigma to be (123) in S5
sigma = S5("(1,2,3)")

# call the new function to calculate the conjugacy class
con_class = conjugacy_class(sigma, S5)

# print out the conjugacy class
print(f"The conjugacy class of {sigma} is: {con_class}")


# Another usefull function that we will need in our toolbox is the function defined in the following cell.  This function
# takes in a group and returns all the conjugacy classes of that group.  We first define the function, then give an example.

# In[ ]:


# defines a function that calculates all conjugacy classes of a group.
def all_conjugacy_classes(group):
    # define a list that will hold all the conjugacy classes of the group.
    conjugacy_classes = []
    # for each element in the group, 
    for i in group.list():
        # define a new set that will be the conjugacy class of that element
        conjugates = set(())
        # for each element of the group, add j^{-1}*i*j (remember that Sage 
        # takes this from right to left) to the conjugacy class
        for j in group.list():
            conjugates.add((j^(-1))*i*j)
        # if that conjugate class is not already in the list, add it.
        if conjugates not in conjugacy_classes:
            conjugacy_classes.append(conjugates)
    
    # return the final list of conjugacy classes.
    return conjugacy_classes


# Here we have an example of how to use this function defined above.  We calculate all of the conjugacy classes of $S_4$.

# In[ ]:


# define the group S4
S4 = SymmetricGroup(4)

# call the function to calculate all conjugacy classes, and store the
# result in cc
cc = all_conjugacy_classes(S4)

# for each item in cc, print out the item.
print("The conjugacy classes of S4 are:")
for k in cc:
    print(f"{k}")


# Here we also define a function that not only will tell us what the conjugacy classes of a group are, but also which
# elements of the group those conjugacy classes come from.  This function takes in a group, and returns a dictionary,
# the keys of which will be the conjugacy classes, and the value of each key is a list of the elements in the group 
# that generate that conjugacy class.

# In[ ]:


# define the function that takes in a group.
def conjugacy_class_gens(group):
    # define the dictionary that will hold all the conjugacy classes,
    # as well as which elements generate those classes.
    conjugacy_classes = {}
    # for each element in the group, 
    for i in group.list():
        # create a new set, that will be the conjugacy class of that element.
        conjugates = set(())
        for j in group.list():
            conjugates.add((j^(-1))*i*j)
        # sort that conjugacy class
        conjugates = sorted(conjugates)
        # if the conjugacy class is already found among the keys of the 
        # dictionary defined above, add the element to it's list, if not,
        # create a new entry with that conjugacy class.
        if str(conjugates) not in conjugacy_classes.keys():
            conjugacy_classes[str(conjugates)] = [i]
        else:
            conjugacy_classes[str(conjugates)].append(i)
    # return the final dictionary with all conjugacy classes and generators.
    return conjugacy_classes


# We demostrate this with the following example.  We calculate all of the conjugacy classes of the group $A_4$. 
# Then print out information about which elements generate each conjugacy class.

# In[ ]:


# define the group A4
A4 = AlternatingGroup(4)

# create the dictionary of all conjugacy classes
cc = conjugacy_class_gens(A4)

# for each (key,value) pair in cc.items(), print out the elements that generate the conjugacy
# class (v), then the conjugacy class (k).
for k,v in cc.items():
    print(f"the elements {v} generate the conjugacy class:\n{k}\n\n")

