import math


class Rectangle:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def area(self):
        area = self.length1 * self.length2
        return area


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area

