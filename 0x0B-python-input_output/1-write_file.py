#!/usr/bin/python3
"""Defines a write_fnfunction."""

def write_file(filename="", text=""):
    """Writes a string to a file
    Args:
        filename:name of the file
        text:string to write
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    return 0
