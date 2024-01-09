#!/usr/bin/python3
"""Defines a class_to_json fn"""


def class_to_json(obj):
    """get the dictionary description of an object

    Args:
        obj:object to retrieve the dictionary from
    Returns:
        dictionary description
    """
    return obj.__dict__
