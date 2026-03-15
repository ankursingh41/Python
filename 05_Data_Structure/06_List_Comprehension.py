# List Comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'melon', 'orange']
print(fruits)
# Create a new list with the first letter of each fruit
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

#Copy the list
new_fruits = fruits + new_fruits
print(new_fruits)