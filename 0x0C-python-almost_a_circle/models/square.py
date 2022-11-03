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
    def size(self, val):
        """setter method for size"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                self
        elif kwargs:
            for attr, val in kwargs.items():
                if attr in dir(self):
                    setattr(self, attr, val)        