#!/usr/bin/env python

class chomped():
    def __init__(self, filename):
        self._filename = filename
        self._file = open(self._filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self._file.readline()
        if line == '':
            self._file.close()
            raise StopIteration()  # end the generator
        return line.rstrip()

mary_in = chomped('DATA/mary.txt')
for line in mary_in:
    print(line)

