#!/usr/bin/env python
# coding: utf-8

# # Cosets 

# This document will be all about exploring cosets in SageMath.  We have previously looked at how to define groups, and how to define elements of those groups as well as performing operations on those elements.  Now we will look at how to perform operations on subgroups of a group, that is calculating the coset of a group.  Recall that for a subgroup $H$ of a group $G$, the left coset of $H$ with respresentative $g\in G$ is defined to be $$ gH=\{gh:h\in H\}.$$ Similarly for right cosets.  Here we define two functions that, when passed a subgroup, and an element of the parent group, will calculate the left coset, or the right coset, respectively.  

# In[ ]:


def left_coset(H, g):
    H_elements = H.list()
    coset = set(())
    for element in H.list():
        coset.add(element*g)
        
    return sorted(coset)

def right_coset(H, g):
    H_elements  = H.list()
    coset = set(())
    for element in H_elements:
        coset.add(g*element)
        
    return sorted(coset)
 


# Here we go through our first example of computing a coset.  Once again, the Integers mod $n$ are implemented in SageMath as a ring, so we will not go through computing a coset with integer groups here, but rather, we begin with the Symmetric Group $S_4$, we take the subgroup $H=\left<(12),(34)\right>$, then we compute the coset of $H$ with representative $(23)$.   

# In[ ]:


# define the symmetric group of order 24
S4 = SymmetricGroup(4)

# define the subgroup H
H = S4.subgroup(['(3,4)','(1,2)'])

# print out the original subgroup
print(H.list())

# select an element from S4
sigma = S4('(2,3)')

# calculate the left coset of H with representative sigma
coset = left_coset(H,sigma)

# print out the coset
print(coset)


# As we have seen in the course, often left and right cosets are not the same.  But another event that occurs frequently, is that two left or two right cosets with different representatives are the same.  The following function gives all the cosets, as well as all the elements of the group that generate that coset, given a subgroup $H$.

# In[ ]:


def coset_generators(H, G):
    cosets  = {}
    for element in G.list():
        
        left_coset = set(())
        right_coset = set(())
        for item in H.list():
            right_coset.add(element*item)
            left_coset.add(item*element)
               
        right_coset = sorted(right_coset)
        left_coset = sorted(left_coset)
        
        
        if str(left_coset) not in cosets.keys() and str(right_coset) not in cosets.keys():
            cosets[str(left_coset)] = [str(element)+"H"]
            cosets[str(right_coset)] = ["H"+str(element)]
        if str(right_coset) in cosets.keys() and str("H"+str(element)) not in cosets[str(right_coset)]:
            cosets[str(right_coset)].append("H"+str(element))
            pass
        if str(left_coset) in cosets.keys() and str(str(element)+"H") not in cosets[str(left_coset)]:
            cosets[str(left_coset)].append(str(element)+"H")
    return cosets


# Here we calculate all the cosets of $H$ in $S_4$, as well as which elements generate those cosets.  This information is stored in the variable `gens`.  Then we calculate the left coset of $H$ with representative $(23)$, and use the information in `gens` to determine what other elements in $S_4$ generate this coset.  

# In[ ]:


gens = coset_generators(H,S4)
print(sigma)
print(H.list())
print(left_coset(H,sigma))
print(gens[str(left_coset(H,sigma))])


# Below, we see the complete information stored in `gens`.  A new programming concept that we are using in this document is the dictionary.  Dictionaries are an object that can not only store values, but keys to reference those values with.  The classical example used is a phisical dictionary, dictionaries are sorted by words, and each word has a definition attached to it.  In a dictionary in python, we define $(\text{key}, \text{value})$ pairs, so that we can access the `value` by calling the `key`.  In the function `coset_generators()` function above, the coset generated is the key, and the value attached to each coset is a list of elements that generate that coset.  Thus in the code above, when we call
# 
# > gens[str(sorted(left_coset(H,sigma))]
# 
# This returns the list of generators that is attached to the left coset of $H$ with representative $\sigma$.

# In[ ]:


for k in gens.keys():
    print(f"{k}")
    for v in gens[k]:
        print(f"\t{v}")


# In the output above, we can see that the left coset and right coset of $H$ with representative $(1324)$ are equal.  Below, we use the original `left_coset` and `right_coset` functions to test to see if this is true.

# In[ ]:


sorted(left_coset(H,S4('(1,3,2,4)')))==sorted(right_coset(H,S4('(1,3,2,4)')))


# Here we make note that SageMath does have a function built in to compute cosets of a given subgroup, although it does not provide us with the additional information of which elements of the group generate that coset.  It is used as follows:

# In[ ]:


S4.cosets(H,side='left')


# In[ ]:


S4.cosets(H,side='right')

