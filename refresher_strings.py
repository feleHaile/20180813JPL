#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'

print("Hello, 'JPL world'!")

print('The "heart" of the matter')

print("""The "heart" of the 'matter' is Play-Dough""")

query = """
select woombas
from quatloos
where name = 'Bob'
"""

s3 = r'spam\n'
s4 = r"spam\n"

x = 50

print(f"There are {x:04d} ways to leave your lover")

print("There are {} ways to leave your lover".format(x))


x = 'foo'
y = b'bar'

print(x.encode())
print(y.decode())








