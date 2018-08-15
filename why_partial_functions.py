#!/usr/bin/env python
from functools import partial

def foo(x, y):
    return y ** x


print(foo(2, 5))

sr = partial(foo, .5)

print(sr(1))
print(sr(2))




