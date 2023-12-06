#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if numbering == search else numbering for numbering in my_list]
