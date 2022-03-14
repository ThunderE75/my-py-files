# Q. Write a Python program to test whether a given letter is a vowel or not.

from crypt import methods


char = input("Enter a Letter: ")

if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
    print(char, 'is a vowel')
else:
    print(char, 'is a Consonant')



# Other methods
# def fun(str):
#     vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

#     if str in vowel:

#         print ("It is a vowel")
#     else:
#         print ("it is not vowel")

# fun('a')
# fun('O')