#!/usr/bin/python3
def simple_delete(a_dictionary, keys=""):
    a_dictionary.pop(keys, None)
    return a_dictionary
