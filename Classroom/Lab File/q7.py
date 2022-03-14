a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))


def is_power(a, b):
    while a % b == 0:
        if a == b:
            return True
        a /= b
    return False

if is_power(a,b):
    print("A is a power of B")
else:
    print("A is a not a power of B")

# print(is_power(6, 2))
# print(is_power(8, 2))