#!/usr/bin/env python

list1 = list()
list2 = ['a', 'b', 'c']
list3 = []
list4 = 'fee fi fo fum'.split()


fruits = ['apple', 'orange', 'lime', 'durian', 'strawberry']

print(len(fruits))

fruits.append('kiwi')

print(fruits, '\n')


more_fruits = ['mangosteen', 'banana', 'watermelon']

fruits.extend(more_fruits)

print(fruits, '\n')

fruits[0] = 'grapefruit'

print(fruits, '\n')

del fruits[3]

print(fruits, '\n')

g = fruits.pop()

print(g)
print(fruits, '\n')


x = fruits.pop(0)
print(x, '\n')

fruits.remove('kiwi')

print(fruits, '\n')

# fruits.remove('marionberry')

f = 'marionberry'
if f in fruits:
    fruits.remove(f)


fruits.insert(4, 'raspberry')

print(fruits, '\n')

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]


print(fruits[0], fruits[-1])

print(fruits[0:3], '\n')

print(fruits[3:len(fruits)])
print(fruits[3:])
print(fruits[:3])
f2 = fruits[:]
f3 = list(fruits)

print(id(fruits), id(f2), id(f3))

print(fruits[::2], '\n')


print(fruits, '\n')


fruits[2:5] = ['fig', 'guava']

print(fruits, '\n')

fruits[3:5] = []

print(fruits, '\n')

x = ['a', 'b', 'c']
y = ['d', 'e', 'f']

m = x + y

print(m)

m = list(x)
m.extend(y)


# x = x + y
#
# y = y + ['g']

m += ['g']





