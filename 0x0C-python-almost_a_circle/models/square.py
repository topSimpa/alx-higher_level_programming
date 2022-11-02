#!/usr/bin/python3
"""defines the square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class a child of Rectangle"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """Initializes a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self):
        """setter method for size"""
        self.width = self.size
        self.height = self.size
