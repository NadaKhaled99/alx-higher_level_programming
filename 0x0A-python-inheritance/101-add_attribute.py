#!/usr/bin/python3
"""function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add attribute to an object if possible

    Args:
        obj:object to add an attribute
        att:name of the attribute to add to obj.
        value:value of att.
    Raises:
        TypeError:If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
