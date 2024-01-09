#!/usr/bin/python3
"""Defines a Rectangle Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """present a square"""

    def __init__(self, size):
        """Initialize a square
        Args:
            size: The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
