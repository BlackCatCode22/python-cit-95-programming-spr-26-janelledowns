int1 = input("Enter a number: ")
int2 = input("Enter a second number: ")
int3 = input("Enter a third number: ")

if int1 > int2:
    if int1 > int3:
        largest = int1
    else :
        largest = int3
else :
    if int2 > int3:
        largest = int2
    else :largest = int3

print(largest)