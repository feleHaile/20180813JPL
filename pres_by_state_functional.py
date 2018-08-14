#!/usr/bin/env python
from collections import Counter

with open('DATA/presidents.txt') as pres_in:
    states = (line.split(':')[6] for line in pres_in)
#    print(list(states))
    counts = Counter(states)

print(counts)

print(counts.most_common(3))
