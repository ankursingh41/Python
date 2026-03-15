n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

Operator = input("Enter operator: ")

match Operator:
    case '+':
        print("Sum is: ", n1 + n2)
    case '-':
        print("Difference is: ", n1 - n2)
    case '*':
        print("Product is: ", n1 * n2)
    case '/':
        if n2 != 0:
            print("Quotient is: ", n1 / n2) 
        else:
            print("Error: Division by zero is not allowed.")
    case '//':
        if n2 != 0:
            print("Floor Division is: ", n1 // n2)
        else:
            print("Error: Division by zero is not allowed.")