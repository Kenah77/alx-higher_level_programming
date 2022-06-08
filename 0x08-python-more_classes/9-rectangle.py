#!/usr/bin/python3
"""
defines Rectangle obj.
"""


class Rectangle:
    """Rectangle obj"""

    instances = 0
    sign = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.instances += 1

    def __str__(self):
        sum = ""
        if self.__height == 0 or self.width == 0:
            return sum
        for x in range(self.__height):
            sum += (str(self.sign) * self.__width)
            if x != self.__height - 1:
                sum += "\n"
        return sum

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.instances -= 1

    @staticmethod
    def bigger_or_equal(rectangle1, rectangle2):
        if not isinstance(rectangle1, Rectangle):
            raise TypeError("rectangle1 must be an instance of Rectangle")
        if not isinstance(rectangle2, Rectangle):
            raise TypeError("rectangle2 must be an instance of Rectangle")
        if rectangle1.area() >= rectangle2.area():
            return rectangle1
        else:
            return rectangle2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value != int(value):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value != int(value):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
