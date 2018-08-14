#!/usr/bin/env python

from threading import Thread, Lock
import random
import time

stuff = []

stuff_lock = Lock()

class SimpleThread(Thread):
    def __init__(self,num):
        super().__init__()  # <1>
        self._threadnum =num

    def run(self): # <2>
        time.sleep(random.randint(1, 3))
        with stuff_lock:
            stuff.append(self._threadnum)
        print("Hello from thread {}".format(self._threadnum))

pool = []
for i in range(10):
    t = SimpleThread(i) # <3>
    t.start() # <4>
    pool.append(t)



print("Done.")

for t in pool:
    t.join()


print(stuff)

