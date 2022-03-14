# Inputs
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
n = int(input('Enter the value of n: '))


def check(a, b, c, n):
    lhs = rhs = 0 
    rhs = a*n + b*n
    lhs = c*n
    # print(rhs,lhs,lhs,rhs)
    if lhs == rhs:
        return True
    else:
        return False

if check(a,b,c,n):
    print('Fermat’s theorem is true')
else: 
    print('Fermat’s theorem is false')

# check(a,b,c,n)
# print(check())
