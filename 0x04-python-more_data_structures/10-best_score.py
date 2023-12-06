#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        s= len(a_dictionary.values())
        if s > 0:
            se = max(a_dictionary.values())
            for key in a_dictionary.keys():
                if a_dictionary[key] == se:
                    return key
    return None
