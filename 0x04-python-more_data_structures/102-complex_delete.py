#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys, values in list(a_dictionary.items()):
        if values is value:
            a_dictionary.pop(keys)
    return a_dictionary
