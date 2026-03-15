def factorial(n) :

    # Base case
    if n==0 or n==1 :
        return 1

    # Recursive case
    ans = n*factorial(n-1)
    return ans

num = int(input("Enter a number : "))
result = factorial(num)
print("Factorial of", num, "is", result)