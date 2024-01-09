#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class BaseGeometry
"""


class Square(Rectangle):
    """inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """for rectangle area"""

        return self.__size ** 2
