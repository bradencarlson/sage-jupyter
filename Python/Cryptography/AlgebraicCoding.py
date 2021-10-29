#!/usr/bin/env python
# coding: utf-8

# # Algebraic Coding Theory

# SageMath provides a great environment to play with the concepts of Algebraic Coding Theory.  If you have not already, I would highly recommend watching Dr. Andrew Misseldine's [Abstract Algebra](https://www.youtube.com/watch?v=Ox-_-D5bMyk&list=PLz7t89zv8Lp2D6xQOG7kUEbN1KP5u-mpH&index=80) videos on Coding Theory and Binary Symmetric Channels, note that the link leads to the first of several videos on this topic.  
# 
# In SageMath, there are a few new topics we need to be introduced to before we can experiment with Group Codes and encoding messages and transmitting them over a binary symmetric channel.  The first is a new class object called a `MatrixSpace`.  Creating a MatrixSpace will allow us to create matrices and utilize them as our encoding and check matrices for our code.  The second is the command `GF(2)`, which specifies a Field of size 2.  We will use this field for our Matrix Space, since `GF(2)` is implemented as the set {0,1} in SageMath.  
# 
# In the code below, we specify two Matrix Spaces, both over `GF(2)`, one of which consists of all 6x3 matrices and the other all 3x6 matrices.  This will give us the tools to define our canonical parity check matrices.  We also define G and H just as Dr. Misseldine defines them in the example he uses in his videos.  

# In[ ]:


Z63_2 = MatrixSpace(GF(2),6,3)
Z36_2 = MatrixSpace(GF(2),3,6)

G = Z63_2([1,0,0, 0,1,0, 0,0,1, 0,1,1, 1,0,1, 1,1,0])
H = Z36_2([0,1,1,1,0,0, 1,0,1,0,1,0, 1,1,0,0,0,1])

print(G)

print()

print(H)


# Here we define yet another Matrix Space, again over `GF(2)`, this time consisting of all 3x1 matrices, this will be the set of all messages we can encode.  we also define one specific message for us to use.  

# In[ ]:


message = MatrixSpace(GF(2),3,1)
x = message([0,0,1])


# Here we define some new classes for our use in this code.  We define the Bernoulli class, which acts as a Bernoulli distribution.  Note that objects of type Bernoulli require a parameter `p`, which will be the probability of success.  We also define the class SymmetricChannel.  This will act as a Binary Symmetric Channel for us to send messages over with some probability of errors.  Each object of type SymmetricChannel needs a Bernoulli distribution to accompany it.  To test whether or not the SymmetricChannel is set up correctly with a Bernoulli distribution, I have provided a function `test()`, which will tell us whether or not our SymmetricChannel is ready to go.  Do not change anything in this cell.

# In[ ]:


import random
class Bernoulli:
    def __init__(self, p):
        self.p = p
    def __repr__(self):
        return f"Bernoulli distribution with parameter {self.p}"
    def randomTrial(self):
        value = random.random()
        if value < self.p:
            return 1
        else:
            return 0

class SymmetricChannel:
    def __init__(self, b):
        if type(b) is Bernoulli:
            self.bernoulli = b
        else:
            self.bernoulli = None
    def __repr__(self):
        return f"A SymmetricChannel based on a Bernoulli distribution with parameter {self.bernoulli.p}"
    def test(self):
        if type(self.bernoulli) is None:
            return "Not set up correctly"
        if type(self.bernoulli) is Bernoulli:
            return "Set up correctly"
    def transmit(self, message):
        if type(message) is sage.matrix.matrix_mod2_dense.Matrix_mod2_dense:
            transmitted = []
            for i in range(0,len(message.rows())):
                value = self.bernoulli.randomTrial()
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
            return matrix(transmitted).transpose()
        else:
            return matrix(message)
        


# Here is our first example of sending a message over the channel, we define a Bernoulli distribution, a SymmetricChannel over that Bernoulli distribution, then we test the channel to ensure that it is set up correctly.  Then in the following cell, we define and encode the message, using our encoding message G, then transmit it over the symmetric channel, we can then perform the check with our matrix H, to see if any errors occured in transmitting.

# In[ ]:


B = Bernoulli(0.05)
T = SymmetricChannel(B)
x = message([0,0,1])
print(T.test())


# In[ ]:


x = message([0,1,0])
encoded = G*x
transmitted = T.transmit(encoded)
checked = H*transmitted

# note that all these matrices are column vectors by default, thus it 
# is much easier to read if you print out the transpose
print(encoded.transpose())
print(transmitted.transpose())
print(checked.transpose())


# By running the above cell several times, occasionally we should see an error apear in the transmitted message, and the check will not come out to be zero.  Since this is a 1-error correcting code, if only one error occurs, we should see the corresponding column of H print out from the check.  If more errors occur, we must request another transmission.