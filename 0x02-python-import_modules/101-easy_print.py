#!/usr/bin/python3
def calculation(a, b):
    from calculation import add, sub
    if a < b:
        g = add(a, b)
        for h in range(4, 6):
            g = add(g, h)
        return g
    else:
        return sub(a, b)
