'''8. Magic Methods
Task: Vector classida __add__ metodini overload qiling.'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, vec):

        return Vector(self.x + vec.x, self.y + vec.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)