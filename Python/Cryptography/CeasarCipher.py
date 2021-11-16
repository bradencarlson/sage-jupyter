#!/usr/bin/env python
# coding: utf-8

# # Ceasar Cipher

# These cells define the digitize and alphabetize functions that will be used to encode messages so that we can do some math 
# with the encoded message. Do not change these cells.

# In[ ]:


def digitize(string):
    cipher_text = []
    for i in string:
        if i == 'A' or i == 'a': cipher_text.append(0)
        if i == 'B' or i == 'b': cipher_text.append(1)
        if i == 'C' or i == 'c': cipher_text.append(2)
        if i == 'D' or i == 'd': cipher_text.append(3)
        if i == 'E' or i == 'e': cipher_text.append(4)
        if i == 'F' or i == 'f': cipher_text.append(5)
        if i == 'G' or i == 'g': cipher_text.append(6)
        if i == 'H' or i == 'h': cipher_text.append(7)
        if i == 'I' or i == 'i': cipher_text.append(8)
        if i == 'J' or i == 'j': cipher_text.append(9)
        if i == 'K' or i == 'k': cipher_text.append(10)
        if i == 'L' or i == 'l': cipher_text.append(11)
        if i == 'M' or i == 'm': cipher_text.append(12)
        if i == 'N' or i == 'n': cipher_text.append(13)
        if i == 'O' or i == 'o': cipher_text.append(14)
        if i == 'P' or i == 'p': cipher_text.append(15)
        if i == 'Q' or i == 'q': cipher_text.append(16)
        if i == 'R' or i == 'r': cipher_text.append(17)
        if i == 'S' or i == 's': cipher_text.append(18)
        if i == 'T' or i == 't': cipher_text.append(19)
        if i == 'U' or i == 'u': cipher_text.append(20)
        if i == 'V' or i == 'v': cipher_text.append(21)
        if i == 'W' or i == 'w': cipher_text.append(22)
        if i == 'X' or i == 'x': cipher_text.append(23)
        if i == 'Y' or i == 'y': cipher_text.append(24)
        if i == 'Z' or i == 'z': cipher_text.append(25)
    return cipher_text
        


# In[ ]:


def alphabetize(digits):
    plain_text = ""
    for i in digits:
        if i == 0: plain_text = plain_text + "A"
        if i == 1: plain_text = plain_text + "B"
        if i == 2: plain_text = plain_text + "C"
        if i == 3: plain_text = plain_text + "D"
        if i == 4: plain_text = plain_text + "E"
        if i == 5: plain_text = plain_text + "F"
        if i == 6: plain_text = plain_text + "G"
        if i == 7: plain_text = plain_text + "H"
        if i == 8: plain_text = plain_text + "I"
        if i == 9: plain_text = plain_text + "J"
        if i == 10: plain_text = plain_text + "K"
        if i == 11: plain_text = plain_text + "L"
        if i == 12: plain_text = plain_text + "M"
        if i == 13: plain_text = plain_text + "N"
        if i == 14: plain_text = plain_text + "O"
        if i == 15: plain_text = plain_text + "P"
        if i == 16: plain_text = plain_text + "Q"
        if i == 17: plain_text = plain_text + "R"
        if i == 18: plain_text = plain_text + "S"
        if i == 19: plain_text = plain_text + "T"
        if i == 20: plain_text = plain_text + "U"
        if i == 21: plain_text = plain_text + "V"
        if i == 22: plain_text = plain_text + "W"
        if i == 23: plain_text = plain_text + "X"
        if i == 24: plain_text = plain_text + "Y"
        if i == 25: plain_text = plain_text + "Z"
    return plain_text
        


# These following cells define the CeasarEncrypt and the CeasarDecrypt functions that will be used to take an 
# encoded message and encrypt it with the CeasarCipher, or any affine cipher that is desired. Do not change these cells. 

# In[ ]:


def CeasarEncrypt(plain_text, a, b):
    message = digitize(plain_text)
    for i in range(0,len(message)):
        message[i] = (a*message[i]+b) % 26
    return alphabetize(message)


# In[ ]:


def CeasarDecrypt(cipher_text, a, b):
    cipher_text = digitize(cipher_text)
    inverse = inverse_mod(a, 26)
    for i in range(0,len(cipher_text)):
        cipher_text[i] = (inverse*cipher_text[i]-inverse*b) % 26
    return alphabetize(cipher_text)
    


# ## Examples

# Here we go through some examples, of defining a message, encrypting that message, and then decrypting the 
# message with the Ceasar Cipher.

# #### Example 1

# In[ ]:


# defined the message to be encoded.  Uses 'x' as a space since 'x' is not a common character
message = "Thisxisxaxsecret"

# encrypts the message to hide from prying eyes, based on the affine cipher y = 5*x+4 mod 26
cipher_text = CeasarEncrypt(message,5,4)

# print the encrypted message
print(cipher_text)

# decrypts the message to read the information.
plain_text = CeasarDecrypt(cipher_text, 5,4)

# prints the plain text to the screen.
print(plain_text)


# #### Example 2 

# In[ ]:


message = "Spaces are not encoded or decoded"
cipher_text = CeasarEncrypt(message,7,25)

print(cipher_text)

# try decrypting with something other than the encryption mapping
plain_text = CeasarDecrypt(cipher_text,19,3)

print(plain_text)

plain_text = CeasarDecrypt(cipher_text,7,25)

print(plain_text)


# Practice encrypting and decrypting messages below with the affine cipher.

# In[ ]:




