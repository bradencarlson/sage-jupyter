#!/usr/bin/env python
# coding: utf-8

# # Fields
# 
# In this part of the project, we will be exploring Fields in SageMath, and some of the functions that are built in 
# to SageMath that help us understand Field Theory.
# 
# Recall that for the Galois Field of order $p^k$, where $p$ is a prime and $k\in \mathbb{Z}$, any field with the same 
# order is isomorphic to this field. In Sage, we implement this as follows.

# In[ ]:


F = GF(8)


# We can also define a Finite Field another way, similar to field obtained when considering the ring $\mathbb{Z}_2[x]$ and modding out by the principle ideal $\left<x^3+x+1\right>$, which is 
# $$ GF(8) = \frac{\mathbb{Z}_2[x]}{\left<x^3+x+1\right>}$$
# Since this is a degree 3 extension.  We can see this by writing the following 
# ```
# F = GF(2^3,'a')
# ```
# Then printing out each element of $F$.  This is shown in the next cell. 
# 

# In[ ]:


F = GF(2^3,'a')
for i in F:
    print(i)


# This can also be done in the following manner:

# In[ ]:


F.<a> = FiniteField(8)
for i in F:
    print(i)


# There are a number of usefull methods that are predefined for us while dealing with these finite fields.  Among these are:
# 
# * `.modulus()` -  returns the modulus of the Field
# * `.multiplicative_order()` - returns the multiplicative order of an element of the Field, to only be used on specific elements of the field. 
# * `factor()` - we will see an example of this is a minute, for this to work, we need to define our fields in the second manner described above. 

# In[ ]:


print(f"The modulus of the field F: {F.modulus()}")
print(f"The multiplicative order of the element a: {a.multiplicative_order()}")


# To factor over a finite field, as mentioned before, we must define the field with an indeterminant, then, specifying a polynomial over that indeterminant, we can use the `factor()` function to factor that polynomial over the finite field.  To see an example of this, consider the following:

# In[ ]:


F.<a> = GF(8)
factor(a^3+a^2)

