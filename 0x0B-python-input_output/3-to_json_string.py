#!/usr/bin/python3
"""Defines a to_json_string fn"""
import json

def to_json_string(my_obj):
    """gets the JSON  of an object

    Args:
        my_obj:object to serialize
    Returns:
        JSON string of the object
    """
    return json.dumps(my_obj)
