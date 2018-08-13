#!/usr/bin/env python
#

class Blorch():
    def __init__(self):
        print("Creating a Blorch")

    def __enter__(self): # <1>
        print("Hi, Mom!")
        return self

    def __exit__(self, exc_type, value, traceback): # <2>
        print("Bye, Mom!")
        if exc_type is not None:
            print('*********************** EXCEPTION ************************')
            print("exception type:", exc_type)  # all None unless Exception occurs
            print("value:", value)
            print("traceback:", traceback)
            print('***********************************************************')
        return True  # <3>

    def laugh(self):
        print("Ha ha ha!")

with Blorch() as b:  # <4>
    print("In the context...")
    b.laugh() # <5>

print('-' * 60)

with Blorch() as b: # <4>
    print("In the context....")
    raise Exception("Oh nooooooo")  # <6>
    b.laugh()  # <7>

