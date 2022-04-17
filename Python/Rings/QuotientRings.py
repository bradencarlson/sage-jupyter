#!/usr/bin/env python
# coding: utf-8

# # Quotient Rings
# 
# Here we will explore some of the implementation of Quotient Rings in SageMath.  We assume that the reader is familiar with the structure of quotient rings, as well as rings in general.  We will deal mostly with Polynomial rings. We can define quotient rings using the `.quotient_ring()` function, here is an example:

# In[ ]:


R.<x> = PolynomialRing(GF(5))
Q.<y> = R.quotient_ring(x^5+2*x)
p = Q(y^3-y)
q = Q(y-4)
p*q


# Note that again, the indeterminant is important, as this is how SageMath recongnizes that any given polynomial belongs to the polynomial ring.  As another example, pulled from the section on Polynomial codes in this class, is 
# given as follows:

# In[ ]:


Z.<y> = PolynomialRing(GF(2))

Z2.<x> = Z.quotient_ring(y^15+1)
p = Z2(1+x^4+x^6+x^7)
q = Z2(1+x+x^4+x^5+x^6+x^9)
p*q


# Here is another example of a quotient ring.

# In[ ]:


Z5 = ZZ.quotient_ring(5)
Z5


# By the First Isomorphism Theorem for Rings, this quotient ring is isomorphic to $\mathbb{Z}_5$. In this project, we 
# will make the most use of Polynomial Rings in one indeterminant. 
