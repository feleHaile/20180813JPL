#!/usr/bin/env python

def next_prime(limit):
    flags = set() #  <1>

    for i in range(2,limit):
        if i in flags:
            continue
        for j in range(2*i,limit+1,i):
            flags.add(j)  # <2>
        yield i  # <3>

np = next_prime(200) # <4>

for prime in np:  # <5>
    print(prime, end=' ')
print('\n\n')

def woowoo():
    yield "Python"
    yield "is"
    yield "fun"


w = woowoo()

for word in w:
    print(word)


def my_range(start=0, stop=10):
    value = start
    while True:
        if value == stop:
            break
        result = value
        value += 1
        yield result

for x in my_range(1, 20):
    print(x)












