def power(a, b) :

    #Base case 
    if b == 0 : return 1

    #Recursive case
    ans = a*power(a, b-1)
    return ans

a = int(input("Enter a : "))
b = int(input("Enter b : "))
result = power(a, b)
print(a, "raised to the power", b, "is", result)
