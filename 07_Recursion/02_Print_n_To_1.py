def print_n_to_1(n) :
    if n == 0 : return  # Base case
    print(n)  # Print the current number
    print_n_to_1(n-1)  # Recursive call with n-1

n = int(input("Enter n : "))
print_n_to_1(n)