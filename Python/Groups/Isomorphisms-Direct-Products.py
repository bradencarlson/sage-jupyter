#!/usr/bin/env python
# coding: utf-8

# # Isomorphisms and Direct Products

# ## Isomorphisms

# Here we explore Isomorphisms in SageMath.  Here we define a group $G$, then we compare it to a few other groups to see if 
# it is isomorphic to that group.

# In[ ]:


G = PermutationGroup(['(1,2)(3,4)','(2,3)(1,4)'])
A4 = AlternatingGroup(4)
K = KleinFourGroup()
S6 = SymmetricGroup(6)
H = CyclicPermutationGroup(4)

print(f"is G isomorphic to A4: {G.is_isomorphic(A4)}")
print(f"is G isomorphic to the Klein Four Group: {G.is_isomorphic(K)}")
print(f"is G isomorphic to S6: {G.is_isomorphic(S6)}")
print(f"is G isomorphic to H: {G.is_isomorphic(H)}")


# An excellent exercise for any student being introduced to groups is to create a permutation group that is isomorphic to 
# the group of rigid motions of a cube.  This can done in the following ways:
# 
# * Note that there are four diagonals, and thus each rigid motion of the cube is some permutation of the diagonals
# * There are eight corners.  Each rigid motion of the cube is some permutation of the corners of the cube
# 
# See if you can come up with this group, when you think you have it, run the code
# 
# > S4 = SymmetricGroup(4)  
# > G.is_isomorphic(S4)
# 
# If you have correctly set up your group, the result will be true.

# ## Direct Products

# SageMath also has functions that can evaluate direct products as well.  The function 
# 
# > direct_product_permgroups([G,H])
# 
# returns the internal direct product of groups `G` and `H` as a permutation group.  We demonstrate this as follows.

# In[ ]:


edp = direct_product_permgroups([A4,H])
edp


# In[ ]:

print("The direct product of A4 and H")
edp.list()


# Below we see the example that $\mathbb{Z}_2\times \mathbb{Z}_2$ is isomorphic to the Klein Four Group.

# In[ ]:


Z1 = CyclicPermutationGroup(2)
Z2 = CyclicPermutationGroup(2)

G = direct_product_permgroups([Z1,Z2])

print("The group G")
print(G.list())

print()
print("Is G isomorphic to K?")
print(G.is_isomorphic(K))

