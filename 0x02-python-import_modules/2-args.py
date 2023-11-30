#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()
argString = "{} argument"
argcharacter = len(sys.argv) - 1
if argcharacter == 0:
    argString += 's.'
elif argcharacter == 1:
    argString += ':'
else:
    argString += 's:'
print(argString.format(argcharacter))

h = 0
for arg in sys.argv:
    if h != 0:
        print("{}: {}".format(h, arg))
    h += 1
