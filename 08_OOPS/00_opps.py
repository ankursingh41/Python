class Student:
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
student1 = Student()
student1.set_name("John")
print(student1.get_name())

Student2 = Student()
Student2.set_name("Alice")
print(Student2.get_name())