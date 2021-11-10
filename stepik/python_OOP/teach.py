class CoordValue:
    def __init__(self, name):
        self.__name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
    
class Point:
    PointX = CoordValue('PointX')
    PointY = CoordValue('PointY')
    def __init__(self,x,y):
        self.PointX = x
        self.PointY = y

p = Point(5,2)
p1 = Point(13,14)
print(p.PointX, p.PointY)
print(p1.PointX, p1.PointY)
