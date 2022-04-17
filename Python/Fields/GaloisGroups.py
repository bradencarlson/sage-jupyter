#!/usr/bin/env python
# coding: utf-8

# # Galois Groups
# 
# Here we will explore Galois Groups in SageMath.  This will require many new functions and classes that we have 
# not yet encountered. Take note of the following 
# * `QuadraticField(a)` forms a field extension over $\mathbb{Q}$ by adjoining the roots of the polynomial $x^2-a$
# * `.galois_group()` retuns the Galois Group of a field extension as a permutation group.  This allows us to 
# use what we already know about groups in sagemath to study the Galois Group.
# * `NumberField(p(x))` forms a field extension over $\mathbb{Q}$ by adjoining a root of the polynomial $p$.  
# We start with an example. 

# In[ ]:


# define a quadratic extension over Q by adjoining sqrt(3)

Q.<s> = QuadraticField(-3)

# define and print the Galois Group
G = Q.galois_group()
G.list()


# There are times where Sage does not want to print out the Galois group, or even produce an element, but can still 
# give us the order of the group, which often helps us to determine what the group is isomorphic to, an example of 
# this follows. 

# In[ ]:


Q.<alpha> = NumberField(x^5+25*x+10)

# print out the degree of the extension
print(Q.absolute_degree())

# print out the order of the Galois Group
G = Q.galois_group('pari')
print(G.order())
G.gens()


# ## Other Extensions
# 
# There are a great many advanced topics that one can look into with regard to these field extensions, but 
# we do not do so here.  In this class, we will mostly be concerned with simple extensions, and splitting fields, 
# so we give a few more examples of both of these. 

# In[ ]:


Q.<a> = QQ.extension(x^3-2)
a^3


# In[ ]:


Q = QQ.algebraic_closure()
pi in Q


# In[ ]:


F = FiniteField(8).extension(x^3-1,'a')
F.order()

