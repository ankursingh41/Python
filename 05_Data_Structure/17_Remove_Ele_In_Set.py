# Using Remove Method
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)  

# Attempting to remove an element that does not exist
try:
    s.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
s.discard(4)
print(s)  

# Attempting to discard an element that does not exist
s.discard(10)  # No error raised
print(s)