#!/usr/bin/python3
def uppercase(str):
    for g in str:
	if ord(g) >= ord('a') and ord(g) <= ord('z'):
            g = chr(ord(g) - 32)
    print("{}".format(g), end="")
    print()
