# Creating a string
name1 = 'Ankur Singh'
name2 = "Anurag"
name3 = '''Aman'''

print(name1, name2, name3)
print(type(name1), type(name2), type(name3))

name4 = '''Im am persuing B. Tech as a
student at NIT Silchar'''
print(name4)

# Indexing in string
print(name1[0])  # Accessing first character
print(name1[-1])  # Accessing last character
print(name1[1:8])  # Accessing characters from index 1 to 7

#Traversing a string
for i in name1 : print(i)

#Using list comprehension to traverse a string
list = [char for char in name1]
print(list)

#find the length of a string
print(len(name1))

#find a char/substring in a string
print(name1.find('ur')) # Returns the index of first occurrence of 'ur'
print(name1.find('Singh')) # Returns the index of first occurrence of 'Singh'