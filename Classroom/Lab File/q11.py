List = [1,(2,3,(4,5,6),7,8),(9,10)]


def nested_sum(L):
    total = total = 0
    for i in range(0,len(L)):
        total = total + nested_sum(L[i])
        total += L[i]
    return total


total = nested_sum(List)
print("Total ->",total)


# *Reference: https://stackoverflow.com/questions/14917092/sum-of-nested-list-in-python






































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