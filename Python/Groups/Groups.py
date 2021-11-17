#!/usr/bin/env python
# coding: utf-8

# # Groups

# Here we dive into groups in SageMath.  There are many different types of groups that we can use in SageMath, including:
# 
# * Symmetric Groups  
# * Dihedral Groups  
# * Alternating Groups
# * The Klein Four Group  
# * The Quaternion Group  
# * And many others
# 
# More information about what named groups are available can be found in your local sage distribution, for example, on my 
# computer, opening the file
# 
# > /usr/lib/python3/dist-packages/sage/groups/perm-gps/pergroup_named.py
# 
# provides much information about other types of groups that can use defined.  Most of these we will not use in this 
# series of documents, but they are there for you to use if would like.  
# 
# We begin with the Dihedral Group.  Considering the symmetries of a triangle, we can define the Dihedral Group of order 
# 3 by writting the following:

# In[ ]:


T = DihedralGroup(3)
T


# To see all of the elements in this group, we can use the `list` command.

# In[ ]:

print("Here we list all the elements of the group T: D3")
T.list()


# In the above list, we see the six elements listed of the Dihedral Group of order six.  SageMath uses a notation that we 
# may not have seen before if we are still being introduced to Groups in Abstract Algebra.  It is refered to as cycle 
# notation, and if you are in an Undergraduate Abstract Algebra class, you will probably be introduced to cycle notation soon.  
# A cycle $ (1,3,2) $ in sage denotes a permutation that sends $1\rightarrow 3$, $3\rightarrow 2$ and $2\rightarrow 1$, they 
# are used extensively in Group theory with permutations.  So in the Dihedral group above, we see the two rotations of a triangle,
# and the three reflections, as well as the identity $()$. 
# 
# We can specify elements of this group by writing the following:

# In[ ]:


sigma = T('(1,3,2)')
tau = T('(2,3)')


# Now that we have some elements from this group, we can perform operations with them, like the following.

# In[ ]:

print("These are the results of the calculations sigma*tau, tau*sigma, sigma^3, and tau^(-1)")
print(sigma*tau)
print(tau*sigma)
print(sigma^3)
print(tau^(-1))


# Note that in SageMath, permutation multiplication is done from LEFT to RIGHT.  
# 
# Some other groups, we can define look like this:

# In[ ]:


S5 = SymmetricGroup(5)
print(f"The order of S5 is {S5.order()}")
print(f"Is S5 abelian? {S5.is_abelian()}")


# Another great function with groups in SageMath is the `cayley_table()` function.  This is used as follows:

# In[ ]:

print("Here we print out the cayley table for T")
T.cayley_table()


# Note that this will be quite large for most groups, usually it will be much too large to be usefull, for example:

# In[ ]:

print("The cayley table for S5")
S5.cayley_table()


# Another great use of SageMath for groups is the `cayley_graph()` function.  It provides a similar operation as the function 
# `cayley_table()` but provides a graphic to visualize the structure of the group.

# In[ ]:

print("This is the cayley graph for T")
T.cayley_graph()


# The other types of groups are declared by using the following syntax:
# 
# * A = AlternatingGroup(n)  
# * Q = QuaternionGroup()  
# * K = KleinFourGroup()  
