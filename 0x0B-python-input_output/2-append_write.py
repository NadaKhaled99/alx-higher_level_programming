#!/usr/bin/python3
"""Defines an append_write fn"""


def append_write(filename="", text=""):
    """Appends a string

    Args:
        filename:name of the file
        text:string to append
    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
    return 0
