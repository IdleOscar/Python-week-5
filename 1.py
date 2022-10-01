class Rectangle:
    def __init__(self,color="green",width=100,height=100,lenth=100):
        self.color = color
        self.width = width
        self.height = height
        self.lenth = lenth
    def cube(self):
        return self.width * self.height * self.lenth
    def square(self):
        return self.width * self.height
rect1=Rectangle()
print(rect1.color)
print(rect1.square())
rect2=Rectangle("yellow",23,34)
print(rect2.color)
print(rect2.square())
rectv3d=Rectangle("red",4,5,6)
print(rectv3d.color)
print(rectv3d.square())
print(rectv3d.cube())