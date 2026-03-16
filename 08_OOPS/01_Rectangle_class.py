class Rectangle:

    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Creating Objects 
rect1 = Rectangle()
rect1.set_dimensions(5, 3)
print("Area of Rectangle 1:", rect1.area())
print("Perimeter of Rectangle 1:", rect1.perimeter())

