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
