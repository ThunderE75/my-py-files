a = input("Enter a String: ")

def reverse(str):
    return str[::-1] #[start:end:step]

b = reverse(a)

if a == b:
    print("Input String is a Pallendrome")
else:
    print("Input String is a Not Pallendrome")

    