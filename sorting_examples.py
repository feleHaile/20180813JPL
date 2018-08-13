#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print(f1, '\n')

# str.lower
f2 = sorted(fruits, key=str.lower)
print(f2, '\n')

f3 = sorted(fruits, key=len)
print(f3, '\n')

def custom_sort(elem):
    return len(elem), elem.lower()

f4 = sorted(fruits, key=custom_sort)
print(f4, '\n')

f4a = sorted(fruits, key=lambda e: (len(e), e.lower()))
print(f4a, '\n')

def wacky(x):
    return x[1].lower()

f5 = sorted(fruits, key=wacky)
print(f5, '\n')








