input_string = input("Enter string: ")
n = int(input("Enter n : "))

#Creating a dictionary for mirror operation
alphabet = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabet = alphabet[::-1]
dict1 = dict(zip(alphabet, reverse_alphabet))

#finding the part of string on which we do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string
mirror = " "
for i in range(0, len(suffix)):
    mirror += dict1[suffix[i]]

#final string after mirror operation
final_string = prefix + mirror
print("Final string after mirror operation:", final_string)