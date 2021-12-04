#!/usr/bin/env python
# coding: utf-8

# # Repeated Squares
# 
# In this document, we discuss the Repeated Squares algorithm, and we discuss one method of implementing this algorithm in SageMath.  Of course, SageMath already contains a function that can perform these operations for us, but this will give us some insight on how a program might perform operations such as
# 
# $$ a^b \mod n $$
# 
# Where both $b$ and $n$ are very large numbers.  The repeated Squares algorithm goes as follows:
# 
# First we need to write $b$ in binary, assume that 
# 
# $$ b=b_n 2^n+b_{n-1}2^{n-1}+\cdots +b_12+b_0 $$
# 
# Where $b_i=0,1$.  Then we compute each of the following:
# 
# \begin{align*}
# a \mod n\\
# a^2 \mod n \\
# (a^2)^2=a^4 \mod n\\
# (a^4)^2=a^8 \mod n\\
# \vdots\\
# a^{2^n}\mod n
# \end{align*}
# 
# Then we can compute
# 
# \begin{eqnarray*} 
# a^b &=& a^{b_n2^n+\cdots+b_12+b_0}\\
# &\equiv& \left(a^{2^n}\right)^{b_n} \left(a^{2^{n-1}}\right)^{b_{n-1}}\cdots \left(a^{2}\right)^{b_1}\left(a\right)^{b_0}\mod n
# \end{eqnarray*}
# 
# Note that during the repeated squares process above, since we can reduce after each step, we never need to deal with any number greater than $n^2-1$.  Thus the final multiplication is managable also reducing at each step.
# 
# Now we will go into how to write a program that can perform this operation in a reasonable amount of time. We will first go into how to write the number $b$ in binary.  We note that by the Division Algorithm, we can write
# 
# $$ b = 2q_0+b_0 \quad\text{where}\quad b_0\in\{0,1\} $$
# 
# Then we could write 
# 
# $$ q_0=2q_1+b_1 \quad\text{where}\quad b_1\in \{0,1\} $$
# 
# And this gives rise to the equation 
# 
# $$ b = 2^2q_1+2b_1+b_0 \quad\text{where}\quad b_i\in\{0,1\}$$
# 
# Continuing this process will give rise to the digits of $b$ in binary, until eventually we reach some $q_n=0$, then the process is complete.  Thus the last digit of $b$ in binary is simply the remainder of $b/2$.  Then if we take the quotient from $b/2$, the next digit is obtained by taking the remainder of the quotient $q_0/2$, and so on.  We demonstrate this in the following code.

# In[ ]:


def to_binary(b: int):
    # if there is a negative number, return an error
    if b < 0:
        return "Please enter positive numbers"
    # otherwise, continue to compute the number in binary
    else:
        # define a new list that will hold all the digits of b in binary
        binary = []
        # define a new variable to represent the quotient, and set
        # it to one so we actually enter the next while loop
        q = 1
        # while the quotient is nonzero...
        while q!=0:
            # find the quotient of b/2
            q = floor(b/2)
            # as well as the remainder
            r = b % 2
            # take the remainder to be the digit of b in
            # binary that we need
            binary.append(r)
            # then set b to be the quotient
            b = q
        # return the list that contains the digits of b in binary
        return binary


# In[ ]:


print(to_binary(13756829))


# NOTE: This function returns the binary digits backwards, that is $b_0$ is first in the list.  This is done for a reason, which we will see later.  Thus the output of the cell above tells us that 
# 
# $$ 13756829 = (110100011110100110011101)_2 $$
# 
# Now we will see the Repeated Squares algorithm in full.  

# In[ ]:


def bin_exp(a: int, b: int, n: int):
    # test to ensure all values are positive.
    if a<0 or b<0 or n<0:
        return "Please enter positive integers only."
    else:
        # create a new list to hold b in binary
        binary = []
        # define quotient to be 1 so we enter the while loop
        q = 1
        # compute b in binary and save the result in reverse in binary list
        while q!=0:
            q = floor(b/2)
            r = b % 2
            binary.append(r)
            b = q
        # define a new list, that currently contains one value: a mod n
        squares = [a % n]
        # up to the length of b in binary, append a^2, a^4, a^8, ... onto the 
        # end of the list, this is done by taking the previous value and squaring
        # it, then reducing mod n
        for i in range(1,len(binary)):
            squares.append(squares[i-1]^2 % n)
        # define a variable to hold the final result
        result = 1
        # go through the list of squares, and if the corresponding binary digit is 1, 
        # then multiply it into the result, and then reduce mod n.
        for i in range(0,len(squares)):
            if binary[i]==1:
                result = (result * squares[i]) % n
        # return the final result
        return result


# Here we go through an example, once using the new function that we have just defined, another using the aritmetic capabilities of SageMath, and we note that the results agree.

# In[ ]:


print(bin_exp(2492872,203583,983))
print(2492872^203583 % 983)

