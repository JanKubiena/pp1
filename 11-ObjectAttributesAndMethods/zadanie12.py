import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return "distance is 0"
        else:
            a = self.x - other.x
            b = self.y - other.y            
            c = math.sqrt(pow(a,2) + pow(b,2))

        if c < 0:
            c = c * -1

        return f'distance is: {c}'    

p1 = Point(10,8)
p2 = Point(6,5)

print(p1 == p2)