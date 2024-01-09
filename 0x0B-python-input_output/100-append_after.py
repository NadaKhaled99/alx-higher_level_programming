#!/usr/bin/python3
'''append_after method'''


def append_after(filename="", search_string="", new_string=""):
    '''inserting text after search string'''
    line = []
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readlines()
        j = 0
        while j < len(line):
            if search_string in line[j]:
                line[j:j + 1] = [line[j], new_string]
                j += 1
            j += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line)
