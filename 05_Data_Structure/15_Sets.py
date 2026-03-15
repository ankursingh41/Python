names = {"Syam", "Ankur", "Sidharth", "Siri", "Ankur", "krishna", "Syam"}

#print set
print(names)

#Check length of set
print(len(names))

#Check data type of set
print(type(names))

#Acessing the item in set
for x in names:
    print(x)

#check if an item exists in set
if "Ankur" in names:
    print("Ankur is part of the set")

#Adding an item to the set
names.add("Ankush")
print(names)

#Add another sequence in a set
new_names = {"Ankush", "Ankit", "Ankur"}
names.update(new_names)
print(names)

#Remove an item from the set
names.remove("Ankur")
print(names)

#Join two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1, set2)
set = set1.union(set2)
print(set)

set1.update(set2)
print(set1)

#Keep only duplicates items while joining two sets
set1.intersection_update(set2)
print(set1)

#Keep all values except duplicates while joining two sets
set1.symmetric_difference_update(set2)
print(set1)
