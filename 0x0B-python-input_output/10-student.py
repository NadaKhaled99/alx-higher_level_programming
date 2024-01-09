#!/usr/bin/python3
"""Define Python class-to-JSON fn"""


def class_to_json(obj):
    """Return dictionary represntation of data structure"""
    return obj.__dict__
