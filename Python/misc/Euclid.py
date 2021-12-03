#!/usr/bin/env python
# coding: utf-8

# # Euclidean Algorithm
# 
# Here we explore one implementation of the Euclidean Algorithm.  Although this may not be the most efficient impelmentation of the Euclidean Algorithm, it is the one I wrote.  Finding the GCD is the easy part of this Algorithm, it is the back substitution that needs some creativity here.  In this document, we will go through the process of developing an algorithm that implements the both sides of the Euclidean Algorithm.
# 
# Here we look at an implementation of the Euclidean Algorithm with no back substitution, that is, it only returns the greatest common divisor of two numbers.  Here we override the gcd function that is provided to us by SageMath, and create our own.  Let's take a look.

# In[ ]:


# define the gcd function that will take in two parameters which must be integers.
def gcd(a,b):
    
    # set the variable atemp to the maximum of the two numbers.
    # Note that we take the absolute value of each of the numbers,
    # as this does not change the gcd.
    atemp = max(abs(a),abs(b))
    
    # similar with btemp, but the minimum.
    btemp = min(abs(a),abs(b))
    
    # let a be the maximum of the two, and b be the minimum of the two, 
    # where both are now positive, if they were not before
    a = atemp
    b = btemp
    
    # while b is non zero...
    while b > 0:
        # obtain the quotient of a/b...
        quotient = floor(a/b)
        # as well as the remainder of a/b...
        remainder = a % b
        # then, for the next step in the Euclidean Algorithm, set
        # a to be the current value of b, and set b to be the remainder 
        # obtained from the previous step, continue this process untill
        # the remainder is zero.
        a = b
        b = remainder
        
    # return the quotient, as this will be the greatest common divisor.
    return a


# Here we give this function a test.  We test a few different numbers, as well as some large ones to demonstrate the speed and efficiency of the Euclidean Algorithm.

# In[ ]:


print(f"gcd(5,12)={gcd(5,12)}")
result = gcd(5^23,23^5)
print(f"gcd(5^23,23^5)={result}")


# Now we turn our attention to the problem of finding some linear combination of the two numbers that equals their gcd.  To see how this is done, consider the following general Euclidean Algorithm:
# \begin{align*}
# a = q_1 b+r_1 \\
# b = q_2 r_1 + r_2 \\
# \vdots \\
# r_{n-2}=q_n r_{n-1}+r_n \\
# r_{n-1}=q_{n+1}r_n 
# \end{align*}
# Where we know that $\gcd(a,b)=r_n$.  We can then work our way back up from the second to last line, we can write
# 
# $$ r_n=r_{n-2}-q_{n}r_{n-1} $$
# But, since 
# 
# $$r_{n-1}=r_{n-3}-q_{n-1}r_{n-2} $$
# 
# We can write
# 
# $$r_n=r_{n-2}-q_n(r_{n-3}-q_{n-1}r_{n-2}) =(1+q_nq_{n-1})r_{n-2}-q_nr_{n-3}$$
# 
# And so on through until we reach the top level, and have some linear combination of $a$ and $b$.  To implement this in an algorithm, we consider the following steps a computer might take. 
# 
# > first, let $x=1$ and $y=-q_n$  
# > then $r_n=xr_{n-2}+yr_{n-1}$  
# > then write $r_n=xr_{n-2}+y(r_{n-3}-q_{n-1}r_{n-2})=(x-q_{n-1}y)r_{n-2}+yr_{n-3}$  
# > set $x=x-q_{n-2}y$ and $y=y$  
# > then $r_n=xr_{n-2}+yr_{n-3}$  
# > then write $r_n=x(r_{n-4}-q_{n-2}r_{n-3})+yr_{n-3}=xr_{n-4}+(y-q_{n-2}x)r_{n-3}$  
# > set $x=x$ and $y=y-q_{n-2}x)$  
# > then $r_n=xr_{n-4}+yr_{n-3}$  
# > continue until we reach the top equation, then we will have a  
# > combination of $a$ and $b$ that equals $r_n=gcd(a,b)$

# In[ ]:


# redefine our gcd function, similar as before, must have
# two intengers as input.
def gcd_full(a: int,b: int):
    # store the original values of a and b into the 
    # variables aOrig and bOrig, to be used at the end
    aOrig = a
    bOrig = b
    
    # let atemp be the maximum of the absolute values of a and b
    # let btemp be the minimum
    atemp = max(abs(a),abs(b))
    btemp = min(abs(a),abs(b))
    
    # reassign the max value to be a and the minimum value to be b
    a = atemp
    b = btemp
    
    # create a list to hold all of the quotients, there is no need to 
    # save all the remainders, as they are not used in the pseudocode 
    # above
    quotients = []
    
    # same as before, go through and perform the steps of the Euclidean
    # algorithm, only this time, save all of the quotients into the list
    # that we just defined.
    while b > 0:
        quotient = floor(a/b)
        remainder = a % b
        a = b
        b = remainder
        quotients.append(quotient)
    
    # let d, be the value of the gcd
    d = a
    
    # throw the very last equation (the one with no remainder)
    # away, since we do not use it in the pseudocode above
    quotients.pop()
    
    # set x and y to their initial values
    x = 1
    y = -quotients.pop()
    
    # set the count equal to one, this will be used to alternate which one of x and y
    # we change in each step
    count = 0
    
    # follow the pseudocode above until there are no longer any quotients left
    while len(quotients)!=0:
        if count % 2 == 0:
            x = x-quotients.pop()*y
        if count % 2 == 1:
            y = y-quotients.pop()*x
        
        count = count + 1
    
    # this part is a little messy (sorry about that), but test to see which linear 
    # combination of the original values of a and b give us the gcd, then
    # return those values
    if x*aOrig+y*bOrig==d:
        return [d,x,y]
    elif (-x)*aOrig+y*bOrig==d:
        return [d,-x,y]
    elif x*aOrig+(-y)*bOrig==d:
        return [d,x,-y]
    elif (-x)*aOrig+(-y)*bOrig==d:
        return [d,-x,-y]
    elif y*aOrig+x*bOrig==d:
        return [d,y,x]
    elif (-y)*aOrig+x*bOrig==d:
        return [d,-y,x]
    elif y*aOrig+(-x)*bOrig==d:
        return [d,y,-x]
    elif (-y)*aOrig+(-x)*bOrig==d:
        return [d,-y,-x]


# Here we go through an example of both of the above methods.  

# In[ ]:


print(gcd(-339348,5423493))
print(gcd_full(-339348,5423493))


# The output of the above cell tells us that
# 
# $$ \gcd(-339348,5423493)=3 $$
# 
# and that
# 
# $$ -339348(-146412)+5423493(-9161)=3 $$
