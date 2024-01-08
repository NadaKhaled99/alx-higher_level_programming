#!/usr/bin/python3
"""
===================================
module inherits_from
===================================
"""
def inherits_from(obj, a_class):
    """Method return True if an object is same  of a class
    which inherited from"""
    return False if type(obj) is a_class else isinstance(obj, a_class)
