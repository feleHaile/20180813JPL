#!/usr/bin/env python
import atexit

def seeya():
    print("See ya later!")

atexit.register(seeya)

for i in 5, 4, 0:
    print(5 / i)




