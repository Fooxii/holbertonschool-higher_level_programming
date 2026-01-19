#!/usr/bin/python3
def print_last_digit(number):
    lastdig = abs(number) % 10
    print(f"{lastdig}",end="")
    return lastdig
