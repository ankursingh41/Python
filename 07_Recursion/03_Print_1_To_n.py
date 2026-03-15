def print_n_to_1(n) :
    if n == 0 : return  # Base case
    print_n_to_1(n-1)  # Recursive call with n-1
    print(n)  # Print the current number

n = int(input("Enter n : "))
print_n_to_1(n)