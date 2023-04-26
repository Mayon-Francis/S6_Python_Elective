class Circle:
    def read(self):
        self.r = int(input("Enter radius: "))
    
    def area(self):
        self.a = 3.14 * self.r * self.r
        print("Area of circle is: ", self.a)
        
    # Used when we want to print the object
    # Should return a string
    def __str__(self):
        return f"Area of circle is: {self.a}, radius is: {self.r}"
        
        
c = Circle()
c.read()
c.area()

print(c)