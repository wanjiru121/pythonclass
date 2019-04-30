class Circle:
    def __init__(self,radius):
        self.radius = radius
    def circle_area(self):
        radius = self.radius
        a = (22/7)*(radius*radius)
        print(a)
    def circumference(self):
        radius = self.radius
        c = 2*(22/7)*radius
        print(c)
class Square:
    def __init__(self,side):
        self.side = side
    def square_area(self):
        side = self.side
        b = side*side
        print(b)
    def perimeter(self):
        side = self.side
        e = 4*side
        print(e)
class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def rect_area(self):
        width = self.width
        length = self.length
        h = width*length
        print(h)
    def perimeter(self):
        width = self.width
        length = self.length
        l = 2*(width+length)
        print(l)
class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def surface_area(self):
        radius = self.radius
        n=4*(22/7)*radius*radius
        print(n)
    def volume(self):
        radius = self.radius
        q = (4/3)*(22/7)*radius*radius*radius
        print(q)