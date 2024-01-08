#!/usr/bin/python3
"""
contain the MyList class
"""
class MyList(list):
    """Implements sorted printing"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
