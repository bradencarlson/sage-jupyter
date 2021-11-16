#!/usr/bin/env python
# coding: utf-8

# # Hill Cipher

# Below is the code to implement the Hill Cipher, which is an example of a **polyalphabetic cryptosystem**, that is, it does 
# not assign a single ciphertext letter to a single plaintext letter, but rather a ciphertext letter may represent more than 
# one plaintext letter.  This example is from Judson's [Abstract Algebra](http://abstract.ups.edu/sage-aata.html) textbook,
# example 7.4.  The encryption is based on the matrix 
# \begin{equation*}
# A=\left(\begin{array}{cc}
# 3 & 5 \\
# 1 & 2
# \end{array}\right)
# \end{equation*}
# and encryptes pairs of letters at a time, rather than one letter at a time.  
# 
# The digitize and alphabetize functions are rather similar to the ones found in the CeasarCipher document, the bigest change 
# being that these pair the numbers up so as to form matrices for encryption and decryption.

# In[ ]:


def digitize(string):
    cipher_text = []
    holder = []
    for i in string:
        if i == 'A' or i == 'a': holder.append(0)
        if i == 'B' or i == 'b': holder.append(1)
        if i == 'C' or i == 'c': holder.append(2)
        if i == 'D' or i == 'd': holder.append(3)
        if i == 'E' or i == 'e': holder.append(4)
        if i == 'F' or i == 'f': holder.append(5)
        if i == 'G' or i == 'g': holder.append(6)
        if i == 'H' or i == 'h': holder.append(7)
        if i == 'I' or i == 'i': holder.append(8)
        if i == 'J' or i == 'j': holder.append(9)
        if i == 'K' or i == 'k': holder.append(10)
        if i == 'L' or i == 'l': holder.append(11)
        if i == 'M' or i == 'm': holder.append(12)
        if i == 'N' or i == 'n': holder.append(13)
        if i == 'O' or i == 'o': holder.append(14)
        if i == 'P' or i == 'p': holder.append(15)
        if i == 'Q' or i == 'q': holder.append(16)
        if i == 'R' or i == 'r': holder.append(17)
        if i == 'S' or i == 's': holder.append(18)
        if i == 'T' or i == 't': holder.append(19)
        if i == 'U' or i == 'u': holder.append(20)
        if i == 'V' or i == 'v': holder.append(21)
        if i == 'W' or i == 'w': holder.append(22)
        if i == 'X' or i == 'x': holder.append(23)
        if i == 'Y' or i == 'y': holder.append(24)
        if i == 'Z' or i == 'z': holder.append(25)
        if len(holder)==2:
            cipher_text.append(matrix(holder))
            holder = []
    if len(holder)==1:
        holder.append(23)
        cipher_text.append(matrix(holder))
    return cipher_text

        


# In[ ]:



def alphabetize(digits):
    plain_text = ""
    comparison = MatrixSpace(IntegerModRing(26),1,1)
    for number in digits:
        for i in number:
            if i == comparison([0])[0]: plain_text = plain_text + "A"
            if i == comparison([1])[0]: plain_text = plain_text + "B"
            if i == comparison([2])[0]: plain_text = plain_text + "C"
            if i == comparison([3])[0]: plain_text = plain_text + "D"
            if i == comparison([4])[0]: plain_text = plain_text + "E"
            if i == comparison([5])[0]: plain_text = plain_text + "F"
            if i == comparison([6])[0]: plain_text = plain_text + "G"
            if i == comparison([7])[0]: plain_text = plain_text + "H"
            if i == comparison([8])[0]: plain_text = plain_text + "I"
            if i == comparison([9])[0]: plain_text = plain_text + "J"
            if i == comparison([10])[0]: plain_text = plain_text + "K"
            if i == comparison([11])[0]: plain_text = plain_text + "L"
            if i == comparison([12])[0]: plain_text = plain_text + "M"
            if i == comparison([13])[0]: plain_text = plain_text + "N"
            if i == comparison([14])[0]: plain_text = plain_text + "O"
            if i == comparison([15])[0]: plain_text = plain_text + "P"
            if i == comparison([16])[0]: plain_text = plain_text + "Q"
            if i == comparison([17])[0]: plain_text = plain_text + "R"
            if i == comparison([18])[0]: plain_text = plain_text + "S"
            if i == comparison([19])[0]: plain_text = plain_text + "T"
            if i == comparison([20])[0]: plain_text = plain_text + "U"
            if i == comparison([21])[0]: plain_text = plain_text + "V"
            if i == comparison([22])[0]: plain_text = plain_text + "W"
            if i == comparison([23])[0]: plain_text = plain_text + "X"
            if i == comparison([24])[0]: plain_text = plain_text + "Y"
            if i == comparison([25])[0]: plain_text = plain_text + "Z"
    return plain_text


# Here we define the HillEncrypt and HillDecrypt functions, which take in strings, and encrypt or decrypt them according 
# to the matrices passed into them as parameters.  

# In[ ]:


def HillEncrypt(message, A, b):
    encoded = digitize(message)
    cipher_text = []
    for item in encoded:
        cipher_text.append(A*item.transpose()+b)
    return alphabetize(cipher_text)

def HillDecrypt(message, A, b):
    A = A.inverse()
    encoded = digitize(message)
    plain_text = []
    for item in encoded:
        plain_text.append(A*item.transpose()-A*b)
    return alphabetize(plain_text)


# Here we use MatrixSpaces over the Ring of integers mod 26, to define the matrices used for encryption and decryption.  
# We use MatrixSpaces rather than ordinary matrices to ensure that the inverse of $A$ is calculated correctly.  

# In[ ]:


Z22_26 = MatrixSpace(IntegerModRing(26),2,2)
Z21_26 = MatrixSpace(IntegerModRing(26),2,1)

# these are the matrices used in the example in the book.
A = Z22_26([[3,5],[1,2]])
b = Z21_26([2,2])


# Here we go through our first example, which is the example in the book, encrypting the message "help".

# In[ ]:


message = "help"
encrypted = HillEncrypt(message,A,b)
print(encrypted)
decrypted = HillDecrypt(encrypted,A,b)
print(decrypted)

