#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newwList = my_list[0:]
    if idx >= 0 and idx <= len(newwList) - 1:
        newwList[idx] = element
        return newwList
    return my_list
