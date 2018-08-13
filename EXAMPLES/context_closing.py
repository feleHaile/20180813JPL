#!/usr/bin/env python
from contextlib import closing

class Spam(): # <1>
    def close(self):  # <2>
        print("I'm outta here...")

with closing(Spam()) as c:
    pass
    # <3>

