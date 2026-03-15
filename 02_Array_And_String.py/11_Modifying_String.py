# For converting Charaters to uppercase

str1 ="new york"
str2 = str1.upper()
print(str2)

# For converting Charaters to lowercase
str3 = str2.lower()
print(str3)

# For converting Charaters to title case
str4 = str1.title()
print(str4)

# Capitalize the first character of the string
str5 = str1.capitalize()
print(str5)

#For stripping /removing  any trailing whitespaces 
str1 = "  Hello World!    "
str6 = str1.strip()
print(str6)

# For replacing a substring with another substring
str7 = str1.replace("Hello", "Hi")
print(str7) 

# For splitting a string into a list of substrings based on a delimiter
str8 = "apple,banana,orange"
str9 = str8.split(",")
print(str9)

#Concatinating two strings
str10 = "Hello"
str11 = "World"
str12 = str10 + " " + str11
print(str12)

#Formatting a string using f-string