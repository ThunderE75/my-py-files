# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

num = int(input('Enter a Number: '))

if (num < 17): 
    num += num
    print(num)
else:
    print(num - 17)

