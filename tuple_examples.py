#!/usr/bin/env python


person = 'Bob', 'Smith', 45, 'Toledo', 'OH'


print(person[0], person[1])


print(len(person))


# UNPACKING!!
first_name, last_name, age, city, state = person


people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'Git'),
]

for person in people:
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name= person[:2]
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, airport in airports.items():
    print(abbr, airport)
print('-' * 60)


colors = ['purple', 'navy', 'chartreuse', 'brown']

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)



print(colors)
print(list(enumerate(colors)))
print(list(enumerate(colors, 1)))
print(list(enumerate(colors, 100)))


letters = ['a', 'b', 'c', 'd', 'e', 'f']

i, j, *k = letters
print(i, j, k)

i, *j, k = letters
print(i, j, k)

*i, j, k = letters
print(i, j, k)















