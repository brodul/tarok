from deck import Deck

import math


class Discard(Deck):
    """"""

    def __init__(self, player):
        self.player = player
        self.cards = []
        self.splitted = []

    def count(self):
        """"""

        self.points = 0
        self.splitted = self.__split_cards(self.cards)
        for trio in self.splitted:
            tmp = 0
            for card in trio:
                tmp += card.weight
            if len(trio) < 3:
                tmp -= 1
            else:
                tmp -= 2
            self.points += tmp
        return self.points

    def __split_cards(self, cards):
        """"""

        splitted = []
        m = int(math.ceil(len(cards) / 3.0))
        for n in range(m):
            splitted.append(cards[n * 3:(n + 1) * 3])
        return splitted
