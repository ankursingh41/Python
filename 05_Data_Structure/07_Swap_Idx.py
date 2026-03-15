n = int(input("Enter the size of list: "))

list = []
for _ in range(n):
    num = int(input("Enter the number: "))
    list.append(num)

print("Original list:", list)

idx1 = int(input("Enter the first index to swap: "))
idx2 = int(input("Enter the second index to swap: "))
# Swap the elements at idx1 and idx2
list[idx1], list[idx2] = list[idx2], list[idx1]

print("List after swapping:", list)
