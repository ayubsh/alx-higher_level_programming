#!/usr/bin/python3
""" Rectangle model module class """
from models.base import Base


class Rectangle(Base):
    """ the rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor for the Rectangle class
        Args:
            width: with of the rectangle
            height: height of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width atrribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """ setter for the width
        Args:
            val: new value
        """
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter for the height atrribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for the height
        Args:
            val: new value
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter for the x atrribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """ setter for x
        Args:
            val: new value
        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter for the y atrribute"""
        return self.__y

    @y.setter
    def y(self, val):
        """ setter for y
        Args:
            val: new value
        """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.height * self.width

    def display(self):
        """ printible rep of the rectangle in # """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for a in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for an in range(self.width)]
            print("")

    def __str__(self):
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)
        return s

    def update(self, *args, **kwargs):
        """ updates rectangle instance """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for kw, v in kwargs.items():
                if kw == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif kw == "width":
                    self.width = v
                elif kw == "height":
                    self.height = v
                elif kw == "x":
                    self.x = v
                elif kw == "y":
                    self.y = v

    def to_dictionary(self):
        """returns dictionary representation of Rectangle """
        d = {"id": self.id, "width": self.width, "height": self.height,
             "x": self.x, "y": self.y}
        return d
