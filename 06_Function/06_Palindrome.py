def is_palindrome(str) :
    # Remove spaces and convert to lowercase
    clean_str = str.replace(" ", "").lower()
    # Reverse the cleaned string
    reverse_str = clean_str[::-1]

    return clean_str == reverse_str


input_string = input("Enter a string : ")

if is_palindrome(input_string) :
    print("The string is a palindrome.")    
else :
    print("The string is not a palindrome.")