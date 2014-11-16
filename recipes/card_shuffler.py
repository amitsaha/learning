'''
A basic card shuffler
'''

from __future__ import print_function
import random

CardDesignation = {
    'jack':11,
    'queen':12,
    'king':13
}

class Card:

    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return self.suite +  ' -> ' + str(self.value)

class Deck:

    def __init__(self):
        self.cards = []
        for suite in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for i in range(1, 11):
                self.cards.append(Card(suite, i))
            for d in CardDesignation.keys():
                self.cards.append(Card(suite, d))

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
for card in deck.cards:
    print(card)
