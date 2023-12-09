#!/usr/bin/python3
def multiple_returns(sentence):
    sl= len(sentence)
    if sl > 0:
        return (sl, sentence[0])
    return (0, None)
