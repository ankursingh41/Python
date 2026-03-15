# Accessing Tuple with Indexing
tup1 = tuple("Geeks")
print(tup1[0])
# Accessing a range of elements using slicing
print(tup1[1:4])  
print(tup1[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")
# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)


# Concatenation of Tuples
tup0 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup0 + tup2
print(tup3)


# Slicing of Tuples
tup4 = tuple('GEEKSFORGEEKS')
# Removing First element
print(tup4[1:])
# Reversing the Tuple
print(tup4[::-1])
# Printing elements of a Range
print(tup4[4:9])


# Delete a Tuple
#Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement
tup5 = (0, 1, 2, 3, 4)
del tup5
print(tup5)  # This will raise an error because tup5 has been deleted

