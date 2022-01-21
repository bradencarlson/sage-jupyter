#!/usr/bin/env python
# coding: utf-8

# # Vigenere Cipher

# Here we will take a look at the Vigenere Cipher.  This cipher is performed by first choosing a secret code word.  The code word is known by both the sending party and the recieving party.  The plaintext and the code word are then both encoded according to some scheme.  We then take the encoded message, and we add the first number of the codeword to the first number of the plaintext, the second number of the codeword to the second letter of the plaintext, and so on until we reach the end of the message, repeating the codeword as many times that is necessary.  Let the secret code word be CAT, and let our encoding scheme be $A\rightarrow 00$, $B\rightarrow 01$, $\dots$, $Z\rightarrow 25$. 
# 
# $$ \begin{array}{ccccccc}
#   & A & T & T & A & C & K \\
#   & 00 & 19 & 19 & 00 & 02 & 10 \\
#   & C & A & T & C & A & T \\
# + & 02 & 00 & 19 & 02 & 00 & 19 \\
# \hline
#   & 02 & 19 & 12 & 02 & 02 & 03 \\
#   & C & T & M & C & C & D
# \end{array} $$
# 
# We can see this implemented in the following code.

# In[ ]:


# this takes a string and converts it into numbers
def digitize(string):
    # create a new array to contains the digitized string
    cipher_text = []
    # for each element of the string, append its corresponding digit to the cipher_text[] array
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
        
# takes a digitized array, and turns it back into the plain text, just as the 
# method above does
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
       
    
# here we define the VignereEncrypt and Decrypt method. 
def VigenereEncrypt(plaintext: str, codeword: str):
    # take in the plaintext string and the keyword,
    # create the digitized array
    ciphertext = digitize(plaintext)
    # create the digitized codeword
    code = digitize(codeword)
    # go through the digitized plaintext and encipher it 
    for i in range(0,len(ciphertext)):
        position = i % len(code)
        ciphertext[i] = (ciphertext[i] + code[position]) % 26
    # return the ciphertext
    return alphabetize(ciphertext)

# do the reverse
def VigenereDecrypt(ciphertext: str, codeword: str):
    # digitize the cipher text
    plaintext = digitize(ciphertext)
    # and the codeword
    code = digitize(codeword)
    # then go through and decode the ciphertext
    for i in range(0,len(plaintext)):
        position = i % len(code)
        plaintext[i] = (plaintext[i] - code[position]) % 26
    # return the plaintext string.
    return alphabetize(plaintext)


# Here we have an example of this code in use.  We use the same message as the example above, as well as the same code word.  We call the `VigenereEncrypt()` method to encrypt the word ATTACK, then we demostrate the `VigenereDecrypt()` function to decrypt the message CTMCCD.

# In[ ]:


print(VigenereEncrypt("Attack", "Cat"))
print(VigenereDecrypt("CTMCCD", "CAT"))

