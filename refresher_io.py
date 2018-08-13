#!/usr/bin/env python

mary_in = open('DATA/mary.txt')
for raw_line in mary_in:
    line = raw_line.rstrip('\n\r')
    print(line)
print('-' * 10)
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
        # m.__exit__()  -> m.close()
print('-' * 10)

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]


with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')


color = input("WHAT is your favorite color? ")

print(f"{color} is delightful! Off you go!")
