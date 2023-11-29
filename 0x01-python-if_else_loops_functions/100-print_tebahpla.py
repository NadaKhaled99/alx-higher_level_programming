#!/usr/bin/python3
h = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:s}".format(chr(c - h)), end="")
    h = 32 if h == 0 else 0
