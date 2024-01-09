#!/usr/bin/python3
"""Defines a from_json_string fn"""
import json


def from_json_string(my_str):
    """inserializes a JSON string

    Args:
        my_str: JSON string to inserialize
    Returns:
        inserialized object
    """
    return json.loads(my_str)
