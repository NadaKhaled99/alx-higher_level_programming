#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()
argcharacter = len(sys.argv) - 1
sult = 0
h = 0
for arg in sys.argv:
    if h != 0:
        sult += int(arg)
    else:
        h += 1
print("{}".format(sult))
