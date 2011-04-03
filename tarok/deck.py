import random


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        if self.suit == 5 and  self.suit > other.suit:
            return 1
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1

    def __repr__(self):
        return str(self.name)


class Tarok(Card):

    rank_list_tarok = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
        "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "IXX",
        "XX", "XXI", "XXII", ]

    # XXX do we really need a rank for Tarok card class
    def __init__(self, suit, rank):
        Card.__init__(self, suit, rank)
        self.name = "Tarok " + self.rank_list_tarok[self.rank - 1]


class Suits(Card):

    suit_list = ["Diamonds", "Hearts", "Spades", "Clubs"]
    rank_list_both = ["Jack", "Horse", "Queen", "King"]
    rank_list_num_red = ["4", "3", "2", "1"]
    rank_list_num_black = ["7", "8", "9", "10"]
    rank_list_red = rank_list_num_red + rank_list_both
    rank_list_black = rank_list_num_black + rank_list_both

    def __init__(self, suit, rank):
        Card.__init__(self, suit, rank)

        if self.suit < 3:
            self.name = self.rank_list_red[self.rank - 1] + \
                " of " + self.suit_list[self.suit - 1]
        if self.suit is 3 or self.suit is 4:
            self.name = self.rank_list_black[self.rank - 1] + \
                " of " + self.suit_list[self.suit - 1]
        self.__set_weight()



class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for rank in range(1, 9):
                self.cards.append(Suits(suit, rank))
        for rank in range(1, 23):
            self.cards.append(Tarok(5, rank))
        for n in range(5):
            self.shuffle()

    def __str__(self):
        string = ""
        for card in self.cards:
            string += "\n" + str(card)
        return string

    def shuffle(self):
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def pop_card(self):
        return self.cards.pop()


class Hand(Deck):

    def __init__(self, label):
        self.label = label
        self.cards = []

    def add_cards(self, number):
        pass
