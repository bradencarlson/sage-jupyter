#!/usr/bin/env python
# coding: utf-8

# # The Group of Integers mod *n*

# In this file, we will talk breifly about using Sage to perform modular arithmetic, and then talk about the Integers mod *n* as a group.  
# 
# The integers mod *n* are implemented as a class called `IntegerModRing` in SageMath.  Hinting at the fact that the integers mod *n* are in fact a ring, even though maybe at this point we may not be aware of that yet.  Below we define `R` to be the set of integers mod 12, then we define two elements `a` and `b` of that group and print out the result when they are added together.  
# 
# As we will see in the future, this representation of a group does not offer us a much as we might wish for, such the ability to print out a Cayley Table, but the integers are simple enough that a computer is not needed to generate the Cayley table for this group.  

# In[ ]:


R = IntegerModRing(12)
a = R(11)
b = R(10)
print(a+b)


# We can also perform multiplication on these numbers, since `R` is in fact a ring not just a group.

# In[ ]:


print(a*b)


# One thing that is peculiar is that the product of two nonzero elements of this ring may be zero, as follows.

# In[ ]:


a = R(3)
b = R(4)

print(a*b)


# You will notice that the following code does not do any modular arithmetic, but rather a regular computation on the integers, this is because up untill now we have been declaring $a$ and $b$ as elements of the ring `R`, as so
# 
# > a = R(3)
# 
# When we specify that $a$ needs to belongs to the ring `R`, then SageMath knows to apply the correct binary operations on that element.

# In[ ]:


# the way we don't want to do this
a = 5
b = 7
print(a+b)

# the way we do want to do this
a = R(5)
b = R(7)
print(a+b)


# ## Other Modular Arithmetic

# Some things that we may not see in group theory as much but can be helpful in SageMath are the modular operations available to us such as:
# 
# > inverse_mod(a,n)  
# > power_mod(a,b,n)
# 
# The first computes the inverse of an element mod *n*, while the second computes $a^b \:\text{mod }n$, for example:

# In[ ]:


print(inverse_mod(5,12))
print(power_mod(5,1023,45))


# For more information about modular arithmetic, visit [Group Theory and Sage](https://doc.sagemath.org/html/en/thematic_tutorials/group_theory.html#group-theory).

# # Modular Arithmetic in Python 
# 
# A side note about modular arithmetic in Python and other programming languages outside of SageMath, when dealing with integers, we can perform modular arithmetic with the `%` operator, like so.

# In[ ]:


print(1243 % 17)


# This computes the remainder of 1243 when divided by 17, or equivalently, 1243 $\text{mod } 17$, We will use this on occasion in this series.  But when performing operations on groups, we will instead use the Ring of Integers from SageMath.
