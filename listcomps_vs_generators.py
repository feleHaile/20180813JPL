#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = (f.upper() for f in fruits)
print("f2:", f2, '\n')

fruits.append('nectarine')

for fruit in f2:
    print(fruit, end=' ')
print('\n\n')

for fruit in f2:
    print(fruit, end=' ')
print('\n\n')


g = (f.upper() for f in fruits)

print(next(g))
print(next(g))

for fruit in g:
    print(fruit, end=' ')
print('\n\n')


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
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = (p[1].upper() for p in people)

for lname in last_names:
    print(lname)

