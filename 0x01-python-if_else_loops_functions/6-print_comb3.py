#!/usr/bin/python3
for i in range(0, 10):
    for z in range(i, 10):
	if i < z:
	    print("{:d}{:d}".format(i, z))
	else:
	    print("{:d}{:d}".format(i, z), end=", ")
