#creating a dictionary
phones = {
    "Ankur": 1234567890,
    "Sidharth": 9876543210,
    "Syam": 5555555555
}

#print the dictionary
print(phones)

#checking the type of the dictionary
print(type(phones))

#checking the length of the dictionary
print(len(phones))

#accessing the value of a key
print(phones["Ankur"]) # print(phones.get("Ankur")) # another way to access the value of a 
print(phones.keys())

#Update the value of a key
phones["Ankur"] = 1111111111
print(phones)

#Adding a new key-value pair to the dictionary
phones["Siri"] = 2222222222
print(phones)

#Removing a key-value pair from the dictionary
phones.pop("Syam")
print(phones)
phones.popitem()  # this will remove the last added item
print(phones)

#Delete the entire dictionary
del phones  
phones.clear() # this will clear the dictionary but it will not delete the dictionary
print(phones) # this will raise an error because phones has been deleted

#printing values of the dictionary
for x, y in phones.items():
    print(x, y)

#Check if a key exists in the dictionary
if "Ankur" in phones:
    print("Ankur is present in the dictionary.")    

#nested dictionary
phones = {
    "CSE" : {
        "Ankur": 1234567890,
        "Sidharth": 9876543210,
        "Syam": 5555555555
    },
    "ECE" : {
        "Ankush": 1111111111,
        "Ankit": 2222222222,
        "Ankur": 3333333333
    }
}
print(phones)
print(phones["CSE"]["Ankur"])
print(phones["ECE"]["Ankur"])