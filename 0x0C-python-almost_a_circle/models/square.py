#!/usr/bin/python3
""" Square class module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class that inherites from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None) -> None:
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                              self.y, self.width)
        return s

    @property
    def size(self):
        """ getter for the size """
        return self.height

    @size.setter
    def size(self, val):
        """ setter for the size """
        self.width = val
        self.height = val

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
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for kw, v in kwargs.items():
                if kw == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif kw == "size":
                    self.size = v
                elif kw == "x":
                    self.x = v
                elif kw == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        d = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return d
