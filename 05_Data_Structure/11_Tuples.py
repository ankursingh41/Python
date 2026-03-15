# Create a tuple
colours = ("red", "yellow", "Green")

# Creating a tuple with 1 item
fruit = ("apple",) # if we remove the comma it is string
fruit = tuple(("apple"))

# Check type of tuple
print(type(colours))

# Check the length oof the tuple
print(len(colours))

# Acessing the item in tuple
print(colours[1]) # positive indexing
print(colours[-1]) # negative indexing
print(colours[1:3]) # range indexing
print(colours[-2:]) # negative range indexing

# Check if an item exists in tuple
if "Green" in colours:
    print("Green is part of tuple")

# Traverse the tuple
for i in colours: 
    print(i)

# Concatenate 2 tuples
colour1 = ("blue", "pruple", "black") 
colours = colours + colour1
print(colours)