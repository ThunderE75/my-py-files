"""
ROT13 is a weak form of encryption that involves "rotating" each letter in a word by 13 places.
To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, 
so 'A' shifted by 3 is 'D' and 'Z' shifted by 1 is 'A'.
"""
# * https://github.com/doubledherin/python-exercises/blob/master/rot13_coder_decoder.py

# x Very - HARD

import string

def rotate_word(s, i):   # s = string, i = seed
    encrypted = []
    
    for c in s:
        if c.islower():
            encrypted += string.lowercase[((string.lowercase).find(c) + i) % 26]
        elif c.isupper():
            encrypted += string.uppercase[((string.uppercase).find(c) + i) % 26]
        else:
            encrypted += c
    
    newstring = ''.join(encrypted)
    
    print (newstring)



si = str(input("Enter a string to encrypt: "))
print(rotate_word(si, 13))








# def rot13_encoder(s):
#     print(rotate_word(s, 13))
    
# def rot13_decoder(s):
#     print(rotate_word(s, -13))
    
    
# rotate_word("CHEERCHEER#$@%%!!!", 7)
# rot13_encoder("In the elevators, the extrovert looks at the OTHER guy's shoes.")
# rot13_decoder("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")