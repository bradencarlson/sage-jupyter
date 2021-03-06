#!/usr/bin/env python
# coding: utf-8

# # Subgroups and Cyclic Groups

# Here we will go over how to define subgroups and cyclic subgroups of the groups that we have already seen.  One way to generate 
# a subgroup of a group is to specify the elements of the subgroup.  For example, consider the group $S_5$, we can define a 
# subgroup of $S_5$, by writing the following:

# In[ ]:


S5 = SymmetricGroup(5)

sigma = S5('(4,5)')
tau = S5('(1,3)')
mu = S5('(1,3)(4,5)')
I = S5('()')

G = S5.subgroup([I,sigma,tau,mu])


# We do need to be sure that we got every member of the group, or at the very least a complete set of generators for this 
# subgroup (in the example above we have every member of the subgroup, as we will soon see), because what this `.subgroup()` 
# function is actually doing is generating the cyclic subgroup generated by the list of elements given as the parameter.  So, 
# in the example above, since these four elements are closed under composition, they form a subgroup of $S_5$.  We can see 
# the complete list of all the elements of the subgroup, and some other atributes in the code below.

# In[ ]:

print("The group G:")
print(G.list())
print()
print(f"The order of G is {G.order()}")
print(f"Is G abelian? {G.is_abelian()}")
print()
print("The cayley table of G:")
print(G.cayley_table())


# One thing the we forgot to mention about those Cayley tables that Sage can produce so nicely for us, while the table itself 
# does not tell us which elements are which (although its not too hard to spot the identity), we can have SageMath print out 
# the values of each column and row label.  For example, say we wanted to know which element SageMath means when it says 
# $b*c=d$ above.  Noting that lists start at position zero, and thus $b$ is in row 1, and $c$ is in column 2, we would type this:

# In[ ]:


T = G.cayley_table()
rows = T.row_keys()
columns = T.column_keys()
print("testing some of the values of T.row_keys() and T.column_keys():")
print(f"b={rows[1]}")
print(f"c={columns[2]}")
print(f"d={rows[3]}")


# Or, maybe this is easier, we could simply type:

# In[ ]:


sorted(T.translation().items())


# Alternatively, we could use the `change_names()` function to rename the lables for the Cayley table. Once again we need to be
# careful here, as we may not necessarily know what order SageMath has the elements (although usually it makes sense the order 
# they are in).  Here we relable the elements to be their cycle notation representation, then we call the `.translation().items()` 
# functions to make sure that each element is matched up correctly, then we print out the Cayley table again, this time knowing 
# exactly which elements are which.  
# 
# See the last example for an example of code that will generate the list of names in the order we want for the cayley table 
# automatically, then assignes those names to the Cayley table.  

# In[ ]:


T.change_names(names=['1','(4,5)','(1,3)','(1,3)(4,5)'])
print("The new cayley table for T:")
print(sorted(T.translation().items()))
T


# As we mentioned before, what SageMath does when we call the `.subgroup()` function is generate the cyclic subgroup based on a 
# list of generators that we pass in as a parameter.  So the following code generates the same subgroup, $G$, that we have 
# been working with up until now, becuase we can find two elements that generate the subgroup $G$. 

# In[ ]:


H = S5.subgroup(['(1,3)','(4,5)'])
print("The groups H and G, respectively:")
print(H.list())
print(G.list())


# Here we go through another example, this time making use of a `for` loop to iterate through each element in the subgroup, to 
# reassign it's name in the Cayley table.  A word of caution: It is very easy to come up with a subgroup whose Cayley table, 
# when the element names are used, is much to large to be readable on the screen.  If that is the case, `.translation().items()` 
# may be a better route.

# In[ ]:


D = SymmetricGroup(6)
G = D.subgroup(['(1,5)','(4,6)'])
T = G.cayley_table()
names = []
for item in G:
    names.append(str(item))
    

print()
print("The result of renaming all the items in T, then the object T:")
print(T.translation().items())
T.change_names(names=names)
print(T)

