#!/usr/bin/env python


class Spam():
    def __init__(self):
        self._id = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

s = Spam()
print(s.id)  # Spam.id_getter(s)
s.id = 42   #  Spam.id_setter(s, 42)
print(s.id)
