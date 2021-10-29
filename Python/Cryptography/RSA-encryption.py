#!/usr/bin/env python
# coding: utf-8

# In[66]:



def PadMessage(message: str, N: int):
    PW = []
    digits = "" 
    for letter in message:
        if letter== "a": digits = digits + "10"; 
        if letter== "b": digits = digits + "11"; 
        if letter== "c": digits = digits + "12";
        if letter== "d": digits = digits + "13"; 
        if letter== "e": digits = digits + "14"; 
        if letter== "f": digits = digits + "15"; 
        if letter== "g": digits = digits + "16"; 
        if letter== "h": digits = digits + "17"; 
        if letter== "i": digits = digits + "18"; 
        if letter== "j": digits = digits + "19"; 
        if letter== "k": digits = digits + "20"; 
        if letter== "l": digits = digits + "21";
        if letter== "m": digits = digits + "22"; 
        if letter== "n": digits = digits + "23"; 
        if letter== "o": digits = digits + "24"; 
        if letter== "p": digits = digits + "25"; 
        if letter== "q": digits = digits + "26"; 
        if letter== "r": digits = digits + "27"; 
        if letter== "s": digits = digits + "28"; 
        if letter== "t": digits = digits + "29"; 
        if letter== "u": digits = digits + "30"; 
        if letter== "v": digits = digits + "31"; 
        if letter== "w": digits = digits + "32"; 
        if letter== "x": digits = digits + "33"; 
        if letter== "y": digits = digits + "34"; 
        if letter== "z": digits = digits + "35"; 
        if letter== "A": digits = digits + "36"; 
        if letter== "B": digits = digits + "37"; 
        if letter== "C": digits = digits + "38"; 
        if letter== "D": digits = digits + "39"; 
        if letter== "E": digits = digits + "40"; 
        if letter== "F": digits = digits + "41"; 
        if letter== "G": digits = digits + "42"; 
        if letter== "H": digits = digits + "43"; 
        if letter== "I": digits = digits + "44"; 
        if letter== "J": digits = digits + "45"; 
        if letter== "K": digits = digits + "46"; 
        if letter== "L": digits = digits + "47"; 
        if letter== "M": digits = digits + "48"; 
        if letter== "N": digits = digits + "49"; 
        if letter== "O": digits = digits + "50"; 
        if letter== "P": digits = digits + "51";
        if letter== "Q": digits = digits + "52"; 
        if letter== "R": digits = digits + "53"; 
        if letter== "S": digits = digits + "54"; 
        if letter== "T": digits = digits + "55"; 
        if letter== "U": digits = digits + "56"; 
        if letter== "V": digits = digits + "57"; 
        if letter== "W": digits = digits + "58"; 
        if letter== "X": digits = digits + "59"; 
        if letter== "Y": digits = digits + "60"; 
        if letter== "Z": digits = digits + "61"; 
        if letter== " ": digits = digits + "62"; 
        if letter== ".": digits = digits + "63"; 
        if letter== ",": digits = digits + "64"; 
        if letter== "?": digits = digits + "65"; 
        if letter== "!": digits = digits + "66";
        if letter== "$": digits = digits + "67"; 
        if letter== "%": digits = digits + "68"; 
        if letter== "&": digits = digits + "69";
        if letter== "0": digits = digits + "70"; 
        if letter== "1": digits = digits + "71"; 
        if letter== "2": digits = digits + "72"; 
        if letter== "3": digits = digits + "73"; 
        if letter== "4": digits = digits + "74"; 
        if letter== "5": digits = digits + "75"; 
        if letter== "6": digits = digits + "76"; 
        if letter== "7": digits = digits + "77"; 
        if letter== "8": digits = digits + "78"; 
        if letter== "9": digits = digits + "79"; 
        if letter== "+": digits = digits + "80"; 
        if letter== "-": digits = digits + "81"; 
        if letter== "*": digits = digits + "82"; 
        if letter== "/": digits = digits + "83"; 
        if letter== "=": digits = digits + "84"; 
        if letter== "^": digits = digits + "85"; 
        if letter== "@": digits = digits + "86"; 
        if letter== "#": digits = digits + "87"; 
        if letter== "(": digits = digits + "88";
        if letter== ")": digits = digits + "89";
        if letter== ";": digits = digits + "90"; 
        if letter== ":": digits = digits + "91"; 
        if letter== "<": digits = digits + "92"; 
        if letter== ">": digits = digits + "93"; 
        if letter== "'": digits = digits + "94"; 
        if letter== "[": digits = digits + "95"; 
        if letter== "]": digits = digits + "96"; 
        if letter== "{": digits = digits + "97"; 
        if letter== "}": digits = digits + "98"; 
        if letter== "_": digits = digits + "99";
        
        if int(digits) > N:
            PW.append(int(digits[0:len(digits)-2]))
            digits = digits[len(digits)-2:]
    if len(digits)!=0:
        PW.append(int(digits))
    return PW


    


# In[59]:


def DepadMessage(digits):
    letters = ""
    plaintext = ""
    for i in digits:
        letters = letters + str(i)
    
    for i in range(0,len(letters)+1,2):
        if letters[i:i+2]== "10": plaintext = plaintext + "a"; 
        if letters[i:i+2]== "11": plaintext = plaintext + "b"; 
        if letters[i:i+2]== "12": plaintext = plaintext + "c"; 
        if letters[i:i+2]== "13": plaintext = plaintext + "d";
        if letters[i:i+2]== "14": plaintext = plaintext + "e"; 
        if letters[i:i+2]== "15": plaintext = plaintext + "f"; 
        if letters[i:i+2]== "16": plaintext = plaintext + "g"; 
        if letters[i:i+2]== "17": plaintext = plaintext + "h"; 
        if letters[i:i+2]== "18": plaintext = plaintext + "i";
        if letters[i:i+2]== "19": plaintext = plaintext + "j";
        if letters[i:i+2]== "20": plaintext = plaintext + "k"; 
        if letters[i:i+2]== "21": plaintext = plaintext + "l"; 
        if letters[i:i+2]== "22": plaintext = plaintext + "m";
        if letters[i:i+2]== "23": plaintext = plaintext + "n"; 
        if letters[i:i+2]== "24": plaintext = plaintext + "o";
        if letters[i:i+2]== "25": plaintext = plaintext + "p"; 
        if letters[i:i+2]== "26": plaintext = plaintext + "q"; 
        if letters[i:i+2]== "27": plaintext = plaintext + "r"; 
        if letters[i:i+2]== "28": plaintext = plaintext + "s";
        if letters[i:i+2]== "29": plaintext = plaintext + "t"; 
        if letters[i:i+2]== "30": plaintext = plaintext + "u"; 
        if letters[i:i+2]== "31": plaintext = plaintext + "v"; 
        if letters[i:i+2]== "32": plaintext = plaintext + "w"; 
        if letters[i:i+2]== "33": plaintext = plaintext + "v"; 
        if letters[i:i+2]== "34": plaintext = plaintext + "y"; 
        if letters[i:i+2]== "35": plaintext = plaintext + "z"; 
        if letters[i:i+2]== "36": plaintext = plaintext + "A"; 
        if letters[i:i+2]== "37": plaintext = plaintext + "B"; 
        if letters[i:i+2]== "38": plaintext = plaintext + "C"; 
        if letters[i:i+2]== "39": plaintext = plaintext + "D"; 
        if letters[i:i+2]== "40": plaintext = plaintext + "E"; 
        if letters[i:i+2]== "41": plaintext = plaintext + "F"; 
        if letters[i:i+2]== "42": plaintext = plaintext + "G"; 
        if letters[i:i+2]== "43": plaintext = plaintext + "H"; 
        if letters[i:i+2]== "44": plaintext = plaintext + "I"; 
        if letters[i:i+2]== "45": plaintext = plaintext + "J"; 
        if letters[i:i+2]== "46": plaintext = plaintext + "K"; 
        if letters[i:i+2]== "47": plaintext = plaintext + "L"; 
        if letters[i:i+2]== "48": plaintext = plaintext + "M"; 
        if letters[i:i+2]== "49": plaintext = plaintext + "N"; 
        if letters[i:i+2]== "50": plaintext = plaintext + "O";
        if letters[i:i+2]== "51": plaintext = plaintext + "P";
        if letters[i:i+2]== "52": plaintext = plaintext + "Q"; 
        if letters[i:i+2]== "53": plaintext = plaintext + "R"; 
        if letters[i:i+2]== "54": plaintext = plaintext + "S"; 
        if letters[i:i+2]== "55": plaintext = plaintext + "T"; 
        if letters[i:i+2]== "56": plaintext = plaintext + "U"; 
        if letters[i:i+2]== "57": plaintext = plaintext + "V"; 
        if letters[i:i+2]== "58": plaintext = plaintext + "W"; 
        if letters[i:i+2]== "59": plaintext = plaintext + "X"; 
        if letters[i:i+2]== "60": plaintext = plaintext + "Y"; 
        if letters[i:i+2]== "61": plaintext = plaintext + "Z"; 
        if letters[i:i+2]== "62": plaintext = plaintext + " "; 
        if letters[i:i+2]== "63": plaintext = plaintext + "."; 
        if letters[i:i+2]== "64": plaintext = plaintext + ","; 
        if letters[i:i+2]== "65": plaintext = plaintext + "?"; 
        if letters[i:i+2]== "66": plaintext = plaintext + "!"; 
        if letters[i:i+2]== "67": plaintext = plaintext + "$"; 
        if letters[i:i+2]== "68": plaintext = plaintext + "%"; 
        if letters[i:i+2]== "69": plaintext = plaintext + "&";
        if letters[i:i+2]== "70": plaintext = plaintext + "0"; 
        if letters[i:i+2]== "71": plaintext = plaintext + "1"; 
        if letters[i:i+2]== "72": plaintext = plaintext + "2"; 
        if letters[i:i+2]== "73": plaintext = plaintext + "3"; 
        if letters[i:i+2]== "74": plaintext = plaintext + "4"; 
        if letters[i:i+2]== "75": plaintext = plaintext + "5"; 
        if letters[i:i+2]== "76": plaintext = plaintext + "6"; 
        if letters[i:i+2]== "77": plaintext = plaintext + "7"; 
        if letters[i:i+2]== "78": plaintext = plaintext + "8"; 
        if letters[i:i+2]== "79": plaintext = plaintext + "9"; 
        if letters[i:i+2]== "80": plaintext = plaintext + "+"; 
        if letters[i:i+2]== "81": plaintext = plaintext + "-"; 
        if letters[i:i+2]== "82": plaintext = plaintext + "*"; 
        if letters[i:i+2]== "83": plaintext = plaintext + "/"; 
        if letters[i:i+2]== "84": plaintext = plaintext + "="; 
        if letters[i:i+2]== "85": plaintext = plaintext + "^"; 
        if letters[i:i+2]== "86": plaintext = plaintext + "@"; 
        if letters[i:i+2]== "87": plaintext = plaintext + "#"; 
        if letters[i:i+2]== "88": plaintext = plaintext + "("; 
        if letters[i:i+2]== "89": plaintext = plaintext + ")";
        if letters[i:i+2]== "90": plaintext = plaintext + ";";
        if letters[i:i+2]== "91": plaintext = plaintext + ":"; 
        if letters[i:i+2]== "92": plaintext = plaintext + "<"; 
        if letters[i:i+2]== "93": plaintext = plaintext + ">"; 
        if letters[i:i+2]== "94": plaintext = plaintext + "'"; 
        if letters[i:i+2]== "95": plaintext = plaintext + "["; 
        if letters[i:i+2]== "96": plaintext = plaintext + "]"; 
        if letters[i:i+2]== "97": plaintext = plaintext + "{"; 
        if letters[i:i+2]== "98": plaintext = plaintext + "}"; 
        if letters[i:i+2]== "99": plaintext = plaintext + "_";
    return plaintext


# In[67]:


def ExpRSA(plaintext, e, N):
    ciphertext = []
    
    for word in plaintext:
        ciphertext.append(power_mod(word, e, N))
        
    return ciphertext


# In[68]:


def EncryptRSA(plaintext, e, N):
    return ExpRSA(PadMessage(plaintext, N), e, N)

def DecryptRSA(ciphertext, d, N):
    return DepadMessage(ExpRSA(ciphertext, d, N))


# In[70]:


n = 3551
e = 629
d = 1997
message = "Here we go again!!!"

encrypted = EncryptRSA(message, e, n)

decrypted  = DecryptRSA(encrypted, 1997, n)

print(encrypted)
print(decrypted)

