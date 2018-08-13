#!/usr/bin/env python
import operator

counts = {}
with open('DATA/presidents.txt') as pres_in:
    for line in pres_in:
        fields = line.split(':')
        state = fields[6]
        if state not in counts:
            counts[state] = 0
        counts[state] += 1


def sort_by_count_then_state(e):
    return -e[1], e[0]

for state, count in sorted(
        counts.items(), key=sort_by_count_then_state):
    print(state, count)
print('-' * 60)

for state, count in sorted(counts.items(), key=operator.itemgetter(1, 0)):
    print(state, count)
print('-' * 60)

