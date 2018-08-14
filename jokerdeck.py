#!/usr/bin/env python

from carddeck import CardDeck

class Dog():
    def bark(self):
        print("Woof! Woof!")

    @property
    def id(self):
        return "I AM DOG"


class JokerDeck(CardDeck, Dog):

    def _create_deck(self):
        super()._create_deck()
        self._cards.append("JOKER1")
        self._cards.append("JOKER2")
