import random

import deck
import end
import game
import subgame


class Game():

    def __init__(self, players):
        self.deck = deck.Deck()
        self.players = players
        self.dealer = random.randint(1, players)
        self.deal()

    def deal(self):
        list = self.deck.deal(self.players)
        self.hands = list[:-1]
        self.talon = list[-1]

    def choose_subgame(self):
        pass
        #doloci igro
        #doloci kralja, ce je taka igra (solo =False)

    def play(self):
        pass
        #while validator podigre
            #karto na mizo
            #validator handov
            #doloci zmagovalca
            #zamenjaj igralca ki igra karto

    def count(self):
        pass

    def points(self):
        pass
