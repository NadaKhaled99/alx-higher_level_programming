#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
	return True
    else:
	return False
def uppercase(str):
    for c in str:
	print("{}".format(chr(ord(c)) if not islower(c) else chr(ord(c)) - 32),
    print("")
