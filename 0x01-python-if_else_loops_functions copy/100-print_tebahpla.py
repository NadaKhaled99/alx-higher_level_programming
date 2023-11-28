#!/usr/bin/python3
for g in range(25, -1, -1):
    f = g + ord('A')
    if g % 2 == 1:
	f = f + 32
    print("{}".format(f), end="")
