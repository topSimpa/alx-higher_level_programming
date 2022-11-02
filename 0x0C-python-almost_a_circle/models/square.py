#!/usr/bin/python3
"""defines the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size: int, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )
