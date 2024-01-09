#!/usr/bin/python3
"""Defines a save_to_json_file fn"""
import json


def save_to_json_file(my_obj, filename):
    """Save object to a file

    Args:
        my_obj:object to save
        filename:name of the save file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
