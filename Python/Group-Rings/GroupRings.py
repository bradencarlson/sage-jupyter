#!/usr/bin/env python
# coding: utf-8

# # Group Rings
# 
# Here we will be exploring Group Rings in SageMath.  As a reminder, to construct a Group Ring, we take a ring $R$, 
# as well as a group $G$, and we construct the set 
# $$ R(G)=\left\{\sum_{g\in G}r_gg\mid r_g\in R\right\}$$
# which is the set of all linear combinations of elements of $G$, with coefficients in the ring $R$.  This produces a new ring, denoted $R(G)$, and can be implemented in SageMath as follows:

# In[ ]:


# define a group 
G = SymmetricGroup(5)

# as well as a ring
R = IntegerModRing(12)

RG = GroupAlgebra(G,R)

RG


# Just like Groups, we can obtain random elements of these Group Rings with the `.random_element()` method.  And we 
# can specify elements that we wish to work with by constructing each piece individually (this is very inconvenient, 
# but I could not find much documentation about constructing elements of group rings, if there is an easier way, please submit an issue on [Github](https://github.com/bradencarlson/sage-jupyter)).  In the following cell, we 
# define the element
# $$ 2(12345)+10(231) \in \mathbb{Z}_{12}(S_5)$$

# In[ ]:


alpha = R(2)*RG(G("(1,2,3,4,5)"))+R(10)*RG(G("(2,3,1)"))


# Note that when defining elements of a Group Ring, we can specify the coefficients as elements of the Ring, instead of elements of the Group.  Since elements of the group ring are present in the calculation, they are upgraded to be 
# elements of the group ring by SageMath.  Although note that the following would be wrong:
# ```
# alpha = R(2)*G("(1,2,3,4,5)")+R(10)*G("(2,3,1)")
# ```
# Since the group elements are not inclosed in `RG(...)`, SageMath does not know that we mean this to be an element of 
# the group ring, but instead throws a TypeError.  
# 
# Note: In addition to the method of constructing group rings that we have already discussed, there is an additional 
# method that is used as follows
# ```
# RG = G.algebra(R)
# ```
# where once again $G$ is a group and $R$ is a ring.  See the following:

# In[ ]:


RG = G.algebra(R)
RG.an_element()


# In addition to the Ring structure of $R(G)$, there are two other operations on the group ring that are important, 
# that is, $*$-involution and $\land$-operation.  These are defined as follows: Given an element 
# $$ a=\sum_{g\in G}\alpha_gg,\quad \alpha_g\in R $$
# Then we define $a^*$ to be the element of $R(G)$ defined by 
# $$ a^*=\sum_{g\in G}\alpha_gg^{-1} $$
# The $\land$-operation is defined by taking a subset $C\subseteq G$, and defining 
# $$ \hat{C}=\sum_{g\in C}g $$
# These operations are implemented by the following functions.

# In[ ]:


def star(a, groupRing):
    element = list(a)
    newElement = RG(0)
    for group,ring in element:
        newElement = newElement + ring*groupRing(group.inverse())
    return newElement



# In[ ]:


sigma = RG.an_element()

print(sigma)
print(star(sigma,RG))

