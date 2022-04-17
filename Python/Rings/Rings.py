#!/usr/bin/env python
# coding: utf-8

# # Rings
# 
# We have already seen many examples of Rings in SageMath, the most common ring that we have used in the 
# `IntegerModRing(n)`.  We can also define other rings, some of the must frequent are 
# * `ZZ` - the ring of Integers
# * `QQ` - the ring of Rational numbers
# * `RR` - the ring of Real numbers
# * `CC` - the ring of Complex numbers
# Another common ring construction is to take a ring $R$, and adjoin an ideterminant to form a polynomal ring.  This 
# is done by writing:
# ```
# RX.<x> = PolynomialRing(R)
# ```
# where $RX$ is the variable name, which can be changed, $x$ is the variable that we adjoin, and $R$ is the ring that 
# was previously selected. Here is an example.

# In[ ]:


RX.<x> = PolynomialRing(QQ)
RX


# We can also define multivariate polynomial rings by writing
# ```
# RX.<x,y> = PolynomialRing(R)
# ```
# where $R$ is a ring.  Note that when we construct these polynomial rings, the indeterminant used has significance, 
# since we might have some code that looks like this:

# In[ ]:


R.<x> = PolynomialRing(QQ)
S.<z> = PolynomialRing(CC)

print(factor(x^2-2))
print(factor(z^2-2))


# These results are different since $x^2-2$ is irreducible over $\mathbb{Q}[x]$, while it splits over $\mathbb{C}[x]$. 
# Here is a more interesting example:

# In[ ]:


R.<x> = PolynomialRing(IntegerModRing(13))
factor(x^2-1)


# Note that while many polynomial rings can be implemented in sagemath in this manner, if the base ring has a 
# composite characteristic, then we recieve an error if we try to factor a polynomal over that ring.  While we can still create the polynomial ring, we cannot use SageMath to factor polymials over that ring.  
# There are many other functions that are very useful when useing Sagemath to study rings, some of which are:
# * `is_commutative()`
# * `is_field()`
# * `is_ring()`
# * `is_finite()`
# * `is_integral_domain()`
# * `is_unique_factorization_domain()`
# * `is_noetherian()`
# * `extension(p)` - extends the ring by forming the quotient $$ \frac{R[x]}{\left<p(x)\right>}$$
# * `ideal(e)` - returns the ideal of the element $e$ in $R$
# * `irreducible_element()`
# * And many others. 
