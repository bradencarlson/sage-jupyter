#!/usr/bin/env python
# coding: utf-8

# # BCH Codes
# 
# Here we will expound on the polynomial codes that we explored in the previous document.  BCH codes are very 
# similar, although we are a little more careful with the choice of the generating polynomial.  Let $d=2r+1$.  Then if 
# $$ g(x)=\text{lcm}\{m_1(x),m_2(x),\dots,m_{2r}(x)\} $$ 
# where $m_i(x)$ is the minimal polynomial of $\omega^i$ where $\omega $ is the primitive $n^{th}$ root of unity 
# over $\mathbb{Z}_2$, then with this choice of $g$, we have that the cyclic code $\left<g(x)\right>$ in 
# $$ \frac{\mathbb{Z}_2[x]}{\left<x^n-1\right>} $$ 
# is called the BHC code of length $n$ and distance $d$.  If we recall the previous results from the Linear codes 
# that were discussed earlier, we have that this code can detect $2r$ errors, and correct $r$ errors.  

# To create a distance 5 BCH code, we take our generating polynomial to be $1+x^4+x^6+x^7+x^8$, which is the product 
# $$ (1+x^2+x^4)(1+x+x^2+x^3+x^4) $$
# This generator polynomial gives a cyclic code with distance 5.  This example is given below.

# In[ ]:


def create_matrix(p,n,A):
    matrix = []
    for i in range(0,n-p.degree()):
        row = p*(x^i)
        row = list(row)
        while len(row)!=n:
            row.append(0)
        matrix.append(row)
    matrix1 = []
    h = (x^n+1)/p
    h = A(h)
    for i in range(0,n-h.degree()):
        h = A(h)
        row = h*(x^i)
        row = A(row)
        row = list(row)
        row.reverse()
        while len(row)<n:
            row.insert(0,0)
        matrix1.append(row)
    #return Matrix(matrix).transpose(), Matrix(matrix1)
    return matrix, matrix1

Z.<x> = PolynomialRing(IntegerModRing(2))
g = 1+x^4+x^6+x^7+x^8
G,H = create_matrix(g,15,Z)

G = Matrix(G).transpose()
H = Matrix(H)
print(H*G)


# Here is an example of a message being encoded and decoded with the matrices defined above. 

# In[ ]:


message = Matrix([0,1,0,1,0,1,0]).transpose()
encoded = G*x
decoded = H*encoded
print(decoded)


# Similarly to what we did with Linear codes, we construct a `BurstChannel` class, which will allow us to "send" 
# our messages across a channel, in which errors could possibly be introduced into our message.  This channel will 
# be different than the `SymmetricChannel` defined before, as this one will have a higher probability of burst errors. 
# Our `BurstChannel` will still be based on the Bernoulli distribution, as before, but will not only depend on this 
# distribution, but also on whether or not an error has previously occured.  We define this now.

# In[ ]:


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
        
class BurstChannel:
    def __init__(self, b, p):
        self.B = Bernoulli(b)
        self.burst = Bernoulli(p)
    def __repr__(self):
        return f"Burst Channel based on {self.B}"
    
    
    def transmit(self,message):
        previous_flip = False
        flip = False
        for i in range(0,len(message)):
            if not previous_flip:
                previous_flip = self.B.randomTrial()
                if previous_flip:
                    message[i] = (message[i]+1) % 2
            else:
                previous_flip = self.burst.randomTrial()
                if previous_flip:
                    message[i] = (message[i]+1) % 2
        return message
            


# Here we define a `BurstChannel` which has a probability of an error of 0.1, but if the previous bit was flipped, 
# then the probability of the next bit having an error is 0.8.  This increases the probability of burst errors.  
# We then define a message, and send it through the Burst Channel, and the print the result.  **Note that in this 
# method, the `BurstChannel` requires a list to be passed into its transmit message, and returns a list, Thus to 
# perform any check with the matrix $H$, we then need to convert the transmitted message to a matrix.**

# In[ ]:


B = BurstChannel(.1,.8)
message = [0,1,1,1,1,0,0]
print(B.transmit(message))


# We will now go through an example of defining generator and parity check matrices, and then using a 
# `BurstChannel` to send our message, and then using the parity check matrix to determine whether or not there were errors in the message. 

# In[ ]:


R.<x> = PolynomialRing(IntegerModRing(2))

p = x^(9)+1

g = x^2+x+1
h = p/g
h = R(h)
G,H = create_matrix(g,9,R)

G = Matrix(G).transpose()
H = Matrix(H)
print(G)
print()
print(H)

message = [0,1,1,1,1,0,0]
message = Matrix(message).transpose()

encoded = G*message

print("encoded: ",encoded.transpose(),"\n")

decoded = H*encoded
print("decoded: ",decoded.transpose())


# Now we will do the same, but we will transmit the message through the `BurstChannel` between encoding, and 
# decoding, and we will see how the syndrome changes as errors are introduced into the message.  **Due to the way the 
# `BurstChannel` was programmed, we add new methods to encode and decode messages, so that we do not have to 
# define our messages with matrices, but can use lists instead.**

# In[ ]:


def encode(message,G):
    message = Matrix(message).transpose()
    encoded = G*message
    encoded = list(encoded.transpose())
    return list(encoded[0])

def decode(message,H):
    message = Matrix(message).transpose()
    decoded = H*message
    decoded = list(decoded.transpose())
    return list(decoded[0])


# Our example of encoded, transmitting, and decoding is below:

# In[ ]:


encoded = encode([0,1,1,1,1,0,0],G)

print("encoded:\t",encoded)

transmitted = B.transmit(encoded)

print("transmitted:\t",transmitted)

decoded = decode(transmitted,H)

print("decoded:\t",decoded)

