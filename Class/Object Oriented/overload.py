class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        temp = Point(0,0)
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp
    
    def __sub__(self, other):
        temp = Point(0,0)
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        return temp
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        d1 = self.x**2 + self.y**2
        d2 = other.x**2 + other.y**2
        return d1 > d2
            
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
p4 = p1 - p2

print(p1)
print(p2)
print(p3)
print(p4)
print(p1==p2)
print(p1<p2)
        
   