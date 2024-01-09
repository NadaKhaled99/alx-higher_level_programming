#!/usr/bin/python3
"""
10-rectangle.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size with integer validator"""
    def __init__(self, size):
        """validar is  un integer for area"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        """super the clase"""
