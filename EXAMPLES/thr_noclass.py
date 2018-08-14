#!/usr/bin/env python

from threading import Thread
import random
import time

def doit(num): # <1>
    time.sleep(random.randint(1, 4))
    print("Hello from thread {}".format(num))

for i in range(10):
    t = Thread(target=doit,args=(1,)) # <2>
    t.start() # <3>
