#!/usr/bin/python3
"""
===================================
module is_kind_of_class
===================================
"""
def is_kind_of_class(obj, a_class):
    """Method that return True if an object is same of a class
    which inherited from"""
    return isinstance(obj, a_class)
