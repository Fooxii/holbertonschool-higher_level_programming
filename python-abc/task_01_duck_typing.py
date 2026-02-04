#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius * self.__radius)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return math.pi * (abs(self.__radius) ** 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.__radius)


def shape_info(argument):
    area = argument.area()
    perimeter = argument.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
