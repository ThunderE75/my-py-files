# my_dict = {"one": 1,"two":2,"three":3,"four":4}

# Python program to sort the list
# alphabetically in a dictionary

dict ={
	"L1":["Banana", "Mango", "Apple"],
	"L2":["Jack", "John", "James"],
	"L3":["portal", "for", "nerds"],
}

print("\nBefore Sorting: ")
for x in dict.items():
	print(x)

print("\nAfter Sorting: ")
for i, j in dict.items():
	sorted_dict ={i:sorted(j)}
	print(sorted_dict)
