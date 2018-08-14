#!/usr/bin/env python


class Spam():
    def __init__(self):
        self.id = 42
        print("constructor")

    def __enter__(self):
        print("Starting the block")
        return self


    def __exit__(self, exc_type, exc, tb):
        print("Leaving the block")


with Spam() as s:
    print("In the block")
    print("s is", s)
    print("s.id is", s.id)

print("Done.")
