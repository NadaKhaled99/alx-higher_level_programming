#!/usr/bin/python3
"""Defines a load_from_json_file fn"""
import json


def load_from_json_file(filename):
    """Create object from a JSON file

    Args:
        filename:name of the file
    Returns:
        inserialized object
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
