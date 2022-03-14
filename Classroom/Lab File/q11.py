L = [1,(2,3,(4,5,6),7,8),(9,10)]


def nested_sum(L):
    sum = 0
    for i in range(0,len(L)):
        sum = sum + nested_sum(L[i])
        #. total += L[i]
    return sum


total = nested_sum(L)
print("Total ->",total)












































# # list = [1,[2,3,[4,5,6],7,8],[9,10]]


# def nested_sum(L):
#     total = 0  # don't use `sum` as a variable name
#     for i in range(len(L)):
#         total =  total + L[i]
        
    
    
    
    
    
#     # for i in L:
#     #     if isinstance(i, list):  # checks if `i` is a list
#     #         total += nested_sum(i)
#     #     else:
#     #         total += i
#     return total

# print(nested_sum(L))