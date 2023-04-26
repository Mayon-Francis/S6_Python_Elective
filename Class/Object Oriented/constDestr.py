class Circle:
    # Constructor
    def __init__(self, x=0):
        self.r = x
    
    def area(self):
        self.a = 3.14 * self.r * self.r
        print("Area of circle is: ", self.a)
        
    # Used when we want to print the object
    # Should return a string
    def __str__(self):
        return f"Area of circle is: {self.a}, radius is: {self.r}"
    
    def __del__(self):
        print("Object destroyed")
        

c = Circle()
c.area()
del(c)
c = Circle(2)
c.area()
print(c)