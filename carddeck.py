#!/usr/bin/env python
import random

class CardDeck():
    SUITS = 'C D H S'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._dealer = None
        self._cards = None

        self.dealer = dealer

        self._create_deck()

    @property
    def id(self):
        return "I AM CARDDECK"

    def _create_deck(self):
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                card = r + s
                self._cards.append(card)


    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")


    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def beep():
        print("Beep! ")
