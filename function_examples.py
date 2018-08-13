#!/usr/bin/env python

def get_message():
    return "Hello, JPL world"

def say_message(message):
    print(message)

m = get_message()
say_message(m)


def spam(x, y='wombat'):
    print(x, y)

spam(1, 2)
spam('hee', 'ha')

spam(5)
spam('marmalade')

# spam(1, 2, 3)


def ham(x, *y):
    print(x, y)

ham(1)
ham(1, 2, 3)
ham(1, 2, 3, 4, 5, 6, 7, 8)


def toast(x, *, user, filename):
    print(user, filename)

toast(5, user='Bob', filename='wombats.txt')
toast(14, filename='wombats.txt', user='Bob')
print()

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

config(username='Bob', filename='wallabies.txt', country='Zambia')


def wacky(p1, p2, *p3, p4, p5, **p6):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print()

wacky(1, 2, p4='spam', p5='ham')
wacky(1, 2, 3, 4, 5, p4='spam', p5='ham', drink='cider', arachnid='black widow spider')

def generic(*args, **kwargs):
    pass


generic()
generic(1, 2, 3)
generic(name='Bob')
generic(1, name='Bob')











