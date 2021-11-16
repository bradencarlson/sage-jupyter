#!/usr/bin/env python
# coding: utf-8

# # Autokey Cipher

# Here we talk about the Autokey Cipher.  This is similar to the Vigenere Cipher, except that instead of a secret code word,
# we choose a secret seed letter.  Then after the initial seed letter is used, the message itself is the keyword used for
# encryption.  We demonstrate this with an example.  Using the same encoding scheme $A\rightarrow 00$, $B\rightarrow 01$, 
# $\dots$, $Z\rightarrow 25$, and choosing our seed letter to be E, we have
# 
# $$
# \begin{array}{ccccccc}
#   & A & T & T & A & C & K \\
#   & 00 & 19 & 19 & 00 & 02 & 10 \\
#   & E & A & T & T & A & C \\
# + & 04 & 00 & 19 & 19 & 00 & 02 \\
# \hline 
#   & 04 & 19 & 12 & 19 & 02 & 12 \\
#   & E & T & M & T & C & M
# \end{array}
# $$
# 
# To decrypt, since we know the seed letter E, if we recieve the message ETMTCM, we encode the message and the seed letter, 
# then we subtract the value of the seed letter from the first letter of the message.  The result, then becomes the number 
# that we must subtract from the second letter of the message, and so on, like so:
# 
# $$
# \begin{array}{ccccccc}
#   & E & T & M & T & C & M \\
#   & 04 & 19 & 12 & 19 & 02 & 12 \\
# - & 04 & 00 & 19 & 19 & 00 & 02 \\
# \hline 
#   & 00 & 19 & 19 & 00 & 02 & 10 \\
#   & A & T & T & A & C & K
# \end{array}
# $$
# 
# We implement this in the following code.

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
        
def AutoKeyEncrypt(plaintext: str, seed: str):
    ciphertext = digitize(plaintext)
    number = digitize(seed)[0]
    for i in range(0,len(ciphertext)):
        temp = ciphertext[i]
        ciphertext[i] = (ciphertext[i] + number) % 26
        number = temp
    return alphabetize(ciphertext)

def AutoKeyDecrypt(ciphertext: str, seed: str):
    plaintext = digitize(ciphertext)
    number = digitize(seed)[0]
    for i in range(0,len(plaintext)):
        plaintext[i] = (plaintext[i] - number) % 26
        number = plaintext[i]
    return alphabetize(plaintext)


# Here we go through the same example as above, to demonstrate the code above.  We encode the message ATTACK, and then 
# decode the same message.

# In[ ]:


print(AutoKeyEncrypt("attack", "e"))


# In[ ]:


print(AutoKeyDecrypt("etmtcm", "e"))

