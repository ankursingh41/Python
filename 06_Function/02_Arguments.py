# Positional Arguments
def add(n1, n2):
    return n1 + n2

result = add(5, 10)
print("Sum:", result)

# Keyword Arguments
def greet(name, greeting):
    print(greeting + ", " + name + "!")

greet(name="Alice", greeting="Hello")
greet(greeting="Hi", name="Bob")

# Default Arguments
def greet_default(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

greet_default("Charlie")
greet_default("David", "Hi")

# Variable-length Arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Sum of all numbers:", sum_all(1, 2, 3, 4, 5))    
