def adder(*args):
    my_sum = 0
    for i in args:
        my_sum += i
    return my_sum

print(adder(2,3,4,5,6,7,8,9,10,11))
print(adder(2,3,4,5,6,10,11))