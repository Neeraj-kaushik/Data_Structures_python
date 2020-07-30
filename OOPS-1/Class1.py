class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        return 3.14*self.radius*self.radius
    def getcircumference(self):
        return 2*3.14*self.radius

radius=int(input())
c1=Circle(radius)
print(c1.getarea())
print(c1.getcircumference())