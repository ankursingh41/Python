# Attributes in Python
# Attributes are variables that belong to an object or class. 
# They are used to store data and represent the state of an object. 

# There are two types of attributes in Python:
# 1. Class attributes --> These are attributes that are specific to an instance of a class. They are defined within the __init__ method and are accessed using the self keyword. Each instance of the class can have different values for these attributes.
# 2. Instance attributes -->  These are attributes that are shared among all instances of a class. They are defined outside of any method and are accessed using the class name or an instance of the class. All instances of the class will have the same value for these attributes.

class Student:
    
    def set_name(self, name):
        self.name = name # This is an class attribute, it is specific to each instance of the Student class.
    
    def get_name(self):
        return self.name
    
student1 = Student()
student1.set_name("John")
print(student1.get_name())
student1.eng_marks = 85 # Adding an instance attribute for student1
print("English Marks of Student 1:", student1.eng_marks)


Student2 = Student()
Student2.set_name("Alice")
print(Student2.get_name())