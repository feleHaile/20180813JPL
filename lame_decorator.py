#!/usr/bin/env python
from functools import wraps

# @foo
# def bar():
#     pass
# bar = foo(bar)

# @spam(x, y)
# def ham():
#     pass
# ham = spam(x, y)()


def more_lame(old_func):

    @wraps(old_func)
    def imposter(*args, **kwargs):
        print("WOOF WOOF")
        return old_func(*args, **kwargs)

    return imposter

# the decorator
def lame(old_func):
    print("Hark! A Decorator!")

    if True:

        @wraps(old_func)
        def imposter(*args, **kwargs):
            print("I am in control!")
            result = old_func(*args, **kwargs)
            return result * 2

        return imposter

    else:
        pass

@lame
def foo():
    print("I am in foo()")
    return 10
# foo = lame(foo)

@more_lame
@lame
def bar():
    print("bar() here")
    return "IKO "

print(foo())
foo()
print(bar())
foo()

print(foo.__name__)
print(bar.__name__)

def outer_deco(bark_type):

    def inner_deco(old_func):
        print("{0} {0}!".format(bark_type))

        @wraps(old_func)
        def imposter(*args, **kwargs):
            result = old_func(*args, **kwargs)
            return result

        return imposter

    return inner_deco



@outer_deco('woof')
def a():
    pass

@outer_deco('ruff')
def b():
    pass

@outer_deco('yip')
def c():
    pass

print(a.__name__)
print(b.__name__)
