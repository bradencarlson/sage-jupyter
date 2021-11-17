#!/usr/bin/env python
# coding: utf-8

# # Frequency Analysis

# Here we define the variables and methods needed to easily perform frequency analysis in order to break the Ceasar Cipher 
# defined earlier in this series of documents.  
# 
# In the cell below, we define an array of all the characters of the English alphabet, as well as a dictionary that 
# corresponds to their encoding, as was defined in the Ceasar Cipher document.  
# 
# If you have not seen dictionaries before, remember that they are a data structure that contains `(key: value)` pairs of data.  

# In[ ]:


alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
alpha = {'a':0, 'b':1,'c':2,'d':3,'e':4,'f':5,
         'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,
         'm':12,'n':13,'o':14,'p':15,'q':16,'r':17,
         's':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}


# Here we define the `create_frequencies()` function, this function reads through the `words.txt` file, which is just a 
# dictionary (a real one, not the data structure discussed above) in .txt form, and counts each letter in the dictionary, 
# then goes through and divides each count by the total number of letters to obtain a percentage for each letter.

# In[ ]:


# Here we define the letter_frequencies dictionary, this is the same dictionary that would be created using SageMath 
# If SageCell had access to the words.txt file found in the project, since SageCell does not have access to this file,
# we instead define the dictionary explicitly, we have also commented out the create_frequencies() function to 
# prevent the user from calling this function and crashing the program.
letter_frequencies = {'a': 0.08028354673082419,
 'h': 0.024342984615100982,
 'e': 0.1177437939585004,
 'd': 0.04119170745646784,
 'i': 0.07500530036964317,
 'n': 0.05773807877731995,
 'g': 0.029569609984974606,
 's': 0.09322197948065596,
 'l': 0.055759888646147324,
 'r': 0.07212189928375874,
 'v': 0.009651281767650231,
 'k': 0.014186554575371256,
 'w': 0.011983444410644986,
 'o': 0.060955172699870025,
 'f': 0.015259533751832085,
 'b': 0.022700330927426418,
 'c': 0.0359890489754155,
 'u': 0.03669883760589217,
 't': 0.05739885512015708,
 'm': 0.028445009817206383,
 'p': 0.029337315524091332,
 'y': 0.018312546666297946,
 'x': 0.0033184922983324574,
 'j': 0.0025957984200289446,
 'z': 0.004387784261128472,
 'q': 0.0018012038752615617}


#def create_frequencies():
#    letters = {}
#    count = 0
#    with open('words.txt', 'r') as file:
#        for word in file:
#            for letter in word:
#                if letter in alphabet:
#                    if letter in letters.keys():
#                        letters[letter.lower()] = letters[letter.lower()]+1
#                    else:
#                        letters[letter.lower()] = 1
#                    count = count+1
#    for k in letters.keys():
#        letters[k] = float(letters[k]/count)
#    return letters


# Here, we define the actual function that will be used to perform frequency analysis.  We go through the ciphertext provided, 
# and find the frequencies of each letter.  Then, we output the five 'most likely' options for the shift cipher. 

# In[ ]:


def analize(ciphertext: str):
    # test the input to ensure that the ciphertext was a string.
    if type(ciphertext)!=str:
        raise Exception("Incorrect type passed to analize function.")
    else:
        # define the dictionary that we will use to store the frequencies.
        frequencies = {}
        count = 0
        # go through each letter in the ciphertext.
        for letter in ciphertext.lower():
            # if that letter is in the alphabet,
            if letter in alphabet:
                # either add it to the frequencies dictionary, or if the key already exists,
                # increment its count.
                if letter in frequencies.keys():
                    frequencies[letter] = frequencies[letter]+1
                else:
                    frequencies[letter] = 1
                count = count + 1
        # go through and divide each count by the total.
        for k in frequencies.keys():
            frequencies[k] = float(frequencies[k]/count)
        # get the frequencies from the english dictionary.
        common = letter_frequencies
        # sort both the ciphertext frequencies and the dictionaries frequencies.
        frequencies_sorted = sorted(((value,key) for (key,value) in frequencies.items()),reverse=True)
        common_sorted = sorted(((value,key) for (key,value) in common.items()),reverse=True)
        most_likely = []
        # get the top five most likely options for the shift cipher.
        for i in range(0,5):
            if frequencies_sorted[0][0]>0.16:
                pos = 1
            else:
                pos = 0
            a = common_sorted[i][1]
            b = frequencies_sorted[pos][1]
            c = alpha[b]-alpha[a]
            most_likely.append((a,b,c % 26))
        # return the most likely options.
        return most_likely


# Here we go through some example.  The following was encrypted using a simple shift cipher.  Can we detect which cipher
# was used without using brute force?

# In[ ]:


analize("MXXTGYMZIUEPAYUEOAZFMUZQPUZFTQEQFIAIADPEIMUFMZPTABQMXQJMZPDQPGYME")

