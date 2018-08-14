#!/usr/bin/env python

def chomped(file_name):
    with open(file_name) as file_name_in:
        for line in file_name_in:
            yield line.rstrip()


mary_in = chomped('DATA/mary.txt')
for line in mary_in:
    print(line)

