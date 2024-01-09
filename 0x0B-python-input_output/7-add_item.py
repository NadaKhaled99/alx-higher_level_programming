#!/usr/bin/python3
"""Defines a JSON file-writing fn"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file-text using JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
