#  A basic cond. while loop
i = 0

while i < 5:
    print(f"This is the {i+1} Line")
    i+=1



#  Another way i to use for loop (very weird)
#  Array should now be called lists

#! This technically works but not ideal
#* Ref: https://youtu.be/ky-24RvI57s?t=935

for i in [0,1,2,3,4]:
    print(f"Line {i+1}")

i = 0  # nullifying it for clarity

#! The better Way to
# range(5) = [0,1,2,3,4,5], range is function

for u in range(5):
    print(f"Line {i}") #h There is no actual counter



#t  Additional Notes
#* Ref: https://youtu.be/ky-24RvI57s?t=1059
# Range can take more than 1 args
# we can set the start, the increment