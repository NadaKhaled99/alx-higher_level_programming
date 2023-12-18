#!/usr/bin/python3
def magic_calculation(a, b):
    relt = 0
    for g in range(1, 3):
        try:
            if g > a:
                raise Exception('Too far')
            else:
                relt += (a ** b) / g
        except (Exception):
            relt = b + a
            break
    return relt
