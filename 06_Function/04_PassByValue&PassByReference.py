# Pass by Value
from turtle import st


def modify(x) :
    x = 10
    print("Inside function :", x)

x = 5
modify(x)
print("Outside function :", x)

# Pass by Reference
def modifyList(lst) :
    lst.append(4)
    print("Inside function :", lst)

lst = [1, 2, 3]
modifyList(lst)
print("Outside function :", lst)