#!/usr/bin/python3
def pow(a, b):
    product = a
    while b != 0:
        product *= a
        b -= 1
    return product
