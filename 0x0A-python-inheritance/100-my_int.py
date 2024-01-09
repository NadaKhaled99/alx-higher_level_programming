#!/usr/bin/python3
"""Defines a class MyInt"""

class MyInt(int):
    """int operators == and !=."""

    def __eq__(self, value):
        """Overide == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Overide != operator with == behavior"""
        return self.real == value
