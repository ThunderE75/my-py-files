num = int(input('Enter a number: '))

#x SUM OF N  or  square of n ?

def sqnum(n):
    ans=0
    for i in range(n, n+1):
        ans = ans + pow(i,2)
    return ans

print(sqnum(num))
# num = 5