#!/usr/bin/env python
from contextlib import contextmanager

@contextmanager
def spam(): # <1>
    yield 25 # <2>
    print("starting exit...") # <3>
    print("...finishing")


with spam() as s:  # <4>
    print("s is", s)
    print("in the context block...")
