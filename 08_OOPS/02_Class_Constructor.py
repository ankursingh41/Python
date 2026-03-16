class Rectangle:

    def __init__(self, length, width):
        print("A rectangle is created with length:", length, "and width:", width)
        self.length = length
        self.width = width

    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Creating Objects   
rect2 = Rectangle(5, 3)
rect1 = Rectangle(4, 3)
# rect1.set_dimensions(5, 3)
print("Area of Rectangle 1 :", rect1.area())
print("Perimeter of Rectangle 1 :", rect1.perimeter())

