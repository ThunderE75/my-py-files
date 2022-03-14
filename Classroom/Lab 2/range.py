# Q. Write a Python program to test whether a number is within 100 or 1000 or 2000 and display appropriate message.

num = int(input('Enter a number: '))

if num < 100:
    print(num, 'is smaller than 100')
elif num < 1000:
    print(num, 'is smaller than 1000')
elif num < 2000:
    print(num, 'is smaller than 2000')
else:
    print(num, 'is larger than 2000')