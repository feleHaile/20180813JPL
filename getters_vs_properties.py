#!/usr/bin/env python

class Person():

    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self._last_name = last_name
        self._city = city

    @property
    def last_name(self):
        return self._last_name

    @property
    def full_name(self):
        return self.first_name + " " + self._last_name


    def get_city(self):
        return self._city


p = Person('Bill', 'Gates', 'Medina')

print(p.first_name, p.last_name)

print(p.full_name)

print(p.get_city())

# p.first_name = {'spam': [1,2,3]}

print(p.full_name)


p.last_name = 'foobar'


