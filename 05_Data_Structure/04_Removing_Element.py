a = [1, 2, 3, 4, 5] # List of integers
fruits = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

a.remove(3) # Remove the first occurrence of 3
print(a)
a.pop(1) # Remove the element at index 1
print(a)
a.pop() # Remove the last element
print(a)

fruits.remove('banana') # Remove 'banana' from the list
print(fruits)
fruits.pop(0) # Remove the element at index 0
print(fruits)
fruits.pop() # Remove the last element
print(fruits)