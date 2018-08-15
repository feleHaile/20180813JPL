#!/usr/bin/env python

from collections import namedtuple

ptuple = 'Fred', 'Jones', 'FL'
plist = ['Fred', 'Jones', 'FL']
pdict = {'first_name': 'Fred', 'last_name': 'Jones', 'state': 'FL'}

print(ptuple[0])
print(plist[0])
print(pdict['first_name'])

fields = 'first_name', 'last_name', 'state'
Wombat = namedtuple('Person', 'first_name last_name state')

pnamed = Wombat('Fred', 'Jones', 'Fl')
print(pnamed[0])
print(pnamed.first_name)

print(pnamed._asdict())
x = pnamed._replace(first_name='Betty')
print(x)
print()
print(pnamed)
print(type(pnamed).__name__)



