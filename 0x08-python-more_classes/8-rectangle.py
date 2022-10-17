#!/usr/bin/python3

""" The Rectangle Class Module """


class Rectangle:
    """for rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constractor/initiliazer for Rectangle class

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter and setter for the width """
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")

        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """ Getter and setter for the height """
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")

        if val < 0:
            raise ValueError("height must be >= 0")

        self.__height = val

    def area(self):
        """ computes the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ computes the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ printible rep of the rectangle in # """
        if self.__height == 0 or self.__width == 0:
            return ""
        pRec = []
        for p in range(self.__height):
            [pRec.append(str(self.print_symbol)) for r in range(self.__width)]
            if p != self.__height - 1:
                pRec.append('\n')
        return (''.join(pRec))

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ detect deletion of instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: if rect_1 or rect_2 not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("ect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
