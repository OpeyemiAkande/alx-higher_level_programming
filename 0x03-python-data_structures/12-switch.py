#!/usr/bin/python3
from base64 import b16encode


a = 89
b = 10
b, a = a, b
print("a={:d} - b={:d}".format(a, b))
