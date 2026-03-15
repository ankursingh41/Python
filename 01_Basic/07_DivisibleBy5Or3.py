n1 = int(input("Enter first number: "))
if(n1 % 15 == 0):
    print(n1, "is divisible by both 5 and 3.")
else:
    if(n1%5 == 0 or n1%3 == 0):
        print(n1, "is divisible by either 5 or 3.")
    else:
        print(n1, "is not divisible by either 5 or 3.")