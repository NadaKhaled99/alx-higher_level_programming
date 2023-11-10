#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultt = 0
    pin = 0
    if type(roman_string) is str and roman_string:
        for j in range(len(roman_string) - 1, -1, -1):
            if values[roman_string[j]] >= pin:
                resultt =resultt + values[roman_string[j]]
            else:
                resultt -= values[roman_string[j]]
            pin = values[roman_string[j]]
    return resultt
