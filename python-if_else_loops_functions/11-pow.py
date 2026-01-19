#!/usr/bin/python3
def pow(a, b):
    product = 1
    while b != 0:
        product *= a
        b -= 1
    return product
