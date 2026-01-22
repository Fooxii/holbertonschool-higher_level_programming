#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    for c in roman_string:
        if c in roman_num:
            total += roman_num[c]
            if prev_num < roman_num[c]:
                total -= prev_num * 2
            prev_num = roman_num[c]
        else:
            return None
    return total
