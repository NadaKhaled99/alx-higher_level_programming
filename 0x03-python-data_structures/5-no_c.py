#!/usr/bin/python3
def no_c(my_string):
    newS = ''
    for a in range(len(my_string)):
        if my_string[a].lower() != 'c':
            newS += my_string[a]
    return newS
