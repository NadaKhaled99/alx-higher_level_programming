#!/usr/bin/python3
def remove_char_at(str, n):
    mstr = ""
    for i, g in enumerate(str):
	if i != n:
	    mstr = mstr + g
    return mstr
