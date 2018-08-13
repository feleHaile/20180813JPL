#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

target = 'x'

# for VAR in ITERABLE: ...

for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print("not found")
print()



for i in range(10):
    print("go CalTech!")
