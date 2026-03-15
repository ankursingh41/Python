n = int(input("Enter the number of rows: "))

for i in range(1,n+1):  # loop for each row
    for j in range(1,n+1): # loop for column
        print(j, end=" ")
    print()