#!/usr/bin/python3
"""Defines a file-text line-counting function."""

def number_of_lines(filename=""):
    """Return the number of lines in a file-text"""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
