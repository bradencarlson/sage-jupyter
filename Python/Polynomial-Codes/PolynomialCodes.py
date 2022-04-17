#!/usr/bin/env python
# coding: utf-8

# # Polynomial Codes
# 
# We can easily identify messages from $\mathbb{Z}_2^{k}$ with a polynomial in $\mathbb{Z}_2[x]$ with the following map
# $$ (a_0,a_1,\dots,a_{k-1})\rightarrow a_0+a_1x+\cdots +a_{k-1}x^{k-1} $$
# If we then fix some nonconstant polynomial $g(x)\in\mathbb{Z}_2[x]$ of degree $n-k$, we can create a $(n,k)$-code defined by multiplication the polynomial $g(x)$.  We will make use of Polynomial Rings in SageMath to implement this 
# here.  Consider the following example, taken from Judson's *Abstract Algebra: Theory and Applications*.  

# In[ ]:


Z.<x> = PolynomialRing(IntegerModRing(2))

# here we are creating a (6,3)-code
g = 1+x^3

# create a codeword f = 011
f = x+x^2

encoded = f*g

print(encoded)

# print the actual binary encoded message
print(list(encoded))


# Here we create a method that generates an encoding message based on an encoding polynomial.  This can then be used 
# to encode messages with out computing the polynomials, although the notions are equivalent.

# In[1]:


def create_matrix(p,n,k):
    matrix = []
    for i in range(0,k):
        row = p*(x^i)
        row = list(row)
        while len(row)<n:
            row.append(0)
        matrix.append(list(row))
    return Matrix(matrix).transpose()


# In[ ]:


m = create_matrix(g,6,3)


# In[ ]:


m


# As demonstrated above, this method requires a polynomial $p$, and the parameters of the code $n$ and $k$.  Now, the 
# next step we wish to take is to use the structure of Rings to improve the codes created.  We desire cyclic codes, 
# and during the course of the [lectures]() corresponding to these documents, we want to consider ideals of the 
# ring 
# $$ \frac{\mathbb{Z}_2[x]}{\left<x^n-1\right>} $$
# which is isomorphic to $\mathbb{Z}_2(Z_n)$ where $Z_n$ is the cyclic group of order $n$. These ideals will need to 
# contain $\left<x^n-1\right>$, and thus as we see in the textbook, as well as in the lectures, a code $C$ is cyclic if and only if it is an ideal of the ring shown above.  
# 
# Say we wish to develop a cyclic code of length 7, then we need some polynomial that divides $x^7-1$.  This can be found by using the `factor` command.

# In[ ]:


factor(x^7+1)


# Choosing our generator polynomial to be $x^3+x^2+1$, we generate a $(7,4)$-block code that will be cyclic.  The 
# generator matrix is found in the following cell.

# In[ ]:


g = x^3+x^2+1
m = create_matrix(g,7,4)
print(m)


# Here we give an example of encoding a message, note that since the encoding matrix is a matrix, we must convert 
# any message into a matrix as well, to avoid TypeErrors.

# In[ ]:


message = Matrix([0,1,1,1]).transpose()
print(m*message)


# We will discuss the detection and correction capabilities of polynomial codes while discussing BCH codes in the next 
# document.
