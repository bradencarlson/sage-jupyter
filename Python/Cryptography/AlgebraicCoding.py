#!/usr/bin/env python
# coding: utf-8

# # Algebraic Coding Theory

# SageMath provides a great environment to play with the concepts of Algebraic Coding Theory.  If you have not already, I would
# highly recommend watching Dr. Andrew Misseldine's 
# [Abstract Algebra](https://www.youtube.com/watch?v=Ox-_-D5bMyk&list=PLz7t89zv8Lp2D6xQOG7kUEbN1KP5u-mpH&index=80) videos on
# Coding Theory and Binary Symmetric Channels, note that the link leads to the first of several videos on this topic.  
# 
# In SageMath, there are a few new topics we need to be introduced to before we can experiment with Group Codes and encoding 
# messages and transmitting them over a binary symmetric channel.  The first is a new class object called a `MatrixSpace`.  
# Creating a MatrixSpace will allow us to create matrices and utilize them as our encoding and check matrices for our code. 
# The second is the command `GF(2)`, which specifies a Field of size 2.  We will use this field for our Matrix Space, since 
# `GF(2)` is implemented as the set {0,1} in SageMath.  
# 
# In the code below, we specify two Matrix Spaces, both over `GF(2)`, one of which consists of all 6x3 matrices and the other 
# all 3x6 matrices.  This will give us the tools to define our canonical parity check matrices.  We also define G and H just 
# as Dr. Misseldine defines them in the example he uses in his videos.  

# In[1]:


Z63_2 = MatrixSpace(GF(2),6,3)
Z36_2 = MatrixSpace(GF(2),3,6)

G = Z63_2([1,0,0, 0,1,0, 0,0,1, 0,1,1, 1,0,1, 1,1,0])
H = Z36_2([0,1,1,1,0,0, 1,0,1,0,1,0, 1,1,0,0,0,1])

print("Matrix used for encoding:")
print(G)

print()

print("Matrix used for checking transmissions:")
print(H)


# Here we define yet another Matrix Space, again over `GF(2)`, this time consisting of all 3x1 matrices, this will be the 
# set of all messages we can encode.  we also define one specific message for us to use.  

# In[2]:


message = MatrixSpace(GF(2),3,1)
x = message([0,0,1])


# Here we define some new classes for our use in this code.  We define the Bernoulli class, which acts as a Bernoulli 
# distribution.  Note that objects of type Bernoulli require a parameter `p`, which will be the probability of success. 
# We also define the class SymmetricChannel.  This will act as a Binary Symmetric Channel for us to send messages over 
# with some probability of errors.  Each object of type SymmetricChannel needs a Bernoulli distribution to accompany it.
# To test whether or not the SymmetricChannel is set up correctly with a Bernoulli distribution, I have provided a function 
# `test()`, which will tell us whether or not our SymmetricChannel is ready to go.  Do not change anything in this cell.

# In[1]:


# import the random module to use in the Bernoulli class
import random

# define the Bernoulli class
class Bernoulli:
    # define the constructor, that requires a parameter p, which should
    # be between zero and one.
    def __init__(self, p):
        self.p = p
    
    # define the method that will display information about the 
    # object when in a print statement
    def __repr__(self):
        return f"Bernoulli distribution with parameter {self.p}"
    
    # define the method that performs a random trial from the 
    # Bernoulli distribution based on the parameter p
    def randomTrial(self):
        value = random.random()
        if value < self.p:
            return 1
        else:
            return 0

# define the SymmetricChannel class
class SymmetricChannel:
    
    # define the constructor, which takes in a bernoulli object
    def __init__(self, b):
        # if b is a Bernoulli assign it to the bernoulli instance in the class,
        # if not, set the bernoulli instance to None
        if type(b) is Bernoulli:
            self.bernoulli = b
        else:
            self.bernoulli = None
            
    # define the method that will provide information about the object when
    # in a print statement
    def __repr__(self):
        return f"A SymmetricChannel based on a Bernoulli distribution with parameter {self.bernoulli.p}"
    
    # define a method to test whether or not the SymmetricChannel has been set up correctly.
    # this just means whether or not the bernoulli object was accepted correctly.
    def test(self):
        if type(self.bernoulli) is None:
            return "Not set up correctly"
        if type(self.bernoulli) is Bernoulli:
            return "Set up correctly"
        
    # this method takes in a matrix, which should be over GF(2), and uses the 
    # bernoulli object to randomly assign errors to the message, to simulate
    # errors we would see over a real channel.
    def transmit(self, message):
        # is the matrix is of the right type, continue to use the Binary Symmetric Channel
        if type(message) is sage.matrix.matrix_mod2_dense.Matrix_mod2_dense:
            transmitted = []
            # for each of the numbers in the message
            for i in range(0,len(message.rows())):
                # take a random trial from the bernoulli distribution.
                value = self.bernoulli.randomTrial()
                # then based on that random trial, either leave the message alone,
                # or commit an error in that bit.
                if value==0:
                    if message[i] == 0:
                        transmitted.append(0)
                    else:
                        transmitted.append(1)
                else:
                    if message[i] == 0:
                        transmitted.append(1)
                    else:
                        transmitted.append(0)
            # return the new message.
            return matrix(transmitted).transpose()
        # if the message was not of the right type, just return it.
        else:
            return matrix(message)
        


# Here is our first example of sending a message over the channel, we define a Bernoulli distribution, a SymmetricChannel 
# over that Bernoulli distribution, then we test the channel to ensure that it is set up correctly.  Then in the following
# cell, we define and encode the message, using our encoding message G, then transmit it over the symmetric channel, we 
# can then perform the check with our matrix H, to see if any errors occured in transmitting.

# In[4]:


# create a Bernoulli object
B = Bernoulli(0.05)

# create a SymmetricChannel based on that Bernoulli distribution
T = SymmetricChannel(B)

# test the SymmetricChannel to ensure that it is ready to receive messages.
print(T.test())


# In[45]:


# define our message
x = message([0,1,0])

# encode the message with the matrix G
encoded = G*x

# transmit the message over the Symmetric Channel
transmitted = T.transmit(encoded)

# Use the matrix H to check for errors
checked = H*transmitted

# print H for reference
print("Matrix used for checking transmissions:")
print(H)
print()

# note that all these matrices are column vectors by default, thus it 
# is much easier to read if you print out the transpose

# print both the message that was transmitted and the syndrome of that 
# message
print(f"Message sent: {encoded.transpose()}") 
print(f"Message recieved: {transmitted.transpose()}")
print(f"Syndrome: {checked.transpose()}")


# By running the above cell several times, occasionally we should see an error apear in the transmitted message, and the 
# check will not come out to be zero.  Since this is a 1-error correcting code, if only one error occurs, we should see 
# the corresponding column of H print out from the check.  If more errors occur, we must request another transmission.
