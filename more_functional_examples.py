#!/usr/bin/env python
import sys
from functools import reduce

values = [5, 10, 15, 20]


def doit(a, b):
    print('->', a, b)
    return a + b


#              func ->    spam(a, b)
total = reduce(doit, values)

print(total)

map(len(list(map(open, sys.argv[1:])))
