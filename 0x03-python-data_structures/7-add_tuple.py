#!/usr/bin/python3
if len(tuple_a) == 0:
        tuple_a += (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0,)
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) == 0:
        tuple_b += (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0,)
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    sumT = tuple(sum(e) for e in zip(tuple_a, tuple_b))
    return sumT
