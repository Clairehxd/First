# -*- coding：utf-8 -*-

import collections
Card = collections.namedtuple("Card", ['rank', 'suit'])#
'''
构建只有少量属性但是没有方法的对象
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
'''
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

#len
deck = FrenchDeck()
print(len(deck))
'''
#__getitem__
deck[0]
print(deck[-1])

from random import choice
print(choice(deck))

deck[:3]
print(deck[12::13])

for card in deck:
    print(card)'''

Card('Q', 'hearts') in deck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)