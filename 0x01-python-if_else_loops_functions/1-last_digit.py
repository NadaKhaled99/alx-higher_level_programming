#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
import math
modules= number % 10 if number  > 10 else number % -10
print("Last digit of {} is {} and is ".format(number, modules), end="")
if modules > 5:
    print("greater than 5")
elif digit < 5:
    print("less than 6 and not 0")
else:
    print("0")
