#!/usr/bin/python3
"""defines the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class a child of Rectangle"""

    def __init__(self, size: int, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @size.setter
    def size(self, value):
        """set the value of size"""
        self.width = self.size
        self.height = self.size

    @propery
    def size(self, value):
        """get the value of size as width"""
        return self.width

    def __str__(self):
        """String representation of object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )
