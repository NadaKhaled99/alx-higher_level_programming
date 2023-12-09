#!/usr/bin/python3
def max_integer(my_list=[]):
    maxint = None
    if len(my_list) > 0:
        maxint = my_list[0]
        for it in my_list:
            if it > maxint:
                maxint = it
    return maxint
