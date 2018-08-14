#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Beverly')
d2 = CardDeck("Manuelo")

print(d1)
print(d1.dealer)

d1.dealer = 'Steve'

print(d1.dealer)

try:
    d1.dealer = ['a', 5, 99]
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)

d1.shuffle()

hand = []
for i in range(5):
    hand.append(d1.draw())
print("Hand:", hand)

print(d1.get_ranks())
print(CardDeck.get_ranks())

d1.beep()
d1.beep()

CardDeck.beep()
print('-' * 60)
j1 = JokerDeck('Albert')
j1.shuffle()

print(j1.draw())
print(j1.cards)


print(JokerDeck.mro())

print(d1.id)
print(j1.id)
j1.bark()

