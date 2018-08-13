#!/usr/bin/env python

d1 = dict()
d2 = {'CA': 'Sacramento', 'NC': 'Raleigh', 'SD': 'Pierre'}
d3 = {}
d4 = dict(CA='Sacramento', NC='Raleigh', SD='Pierre')

pairs = [('CA', 'Sacramento'), ('NC', 'Raleigh'), ('SD', 'Pierre')]

d5 = dict(pairs)

states = ['CA', 'NC', 'SD']
caps = ['Sacramento', 'Raleigh', 'Pierre']

d6 = dict(zip(states, caps))

print(d6)

print(d6['CA'])
d6['NV'] = 'Las Vegas'

print(d6, '\n')

d6['NV'] = 'Carson City'


print(d6, '\n')

print(d6.keys(), '\n')
print(d6.values(), '\n')
print(d6.items(), '\n')

print(len(d6))

print(d6.get('WA'))
# or
print(d6.get('WA', 'NOT FOUND'))
# or
print(d6.setdefault('WA', 'Olympia'))

print(d6, '\n')


#   for key, value in DICT.items(): ...
for state, capitol in d6.items():
    print(state, capitol)
print()

