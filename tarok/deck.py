import random


class Card:
    """Base class for cards"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        """Compare rules for cards

        The tarok card with rank 5 allways wins.
        """

        if self.suit == 5 and  self.suit > other.suit:
            return 1
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        if self.rank == other.rank:
            if self.suit == other.suit:
                raise Exception("No card in deck should be the same")
            else:
                return 0

    def __repr__(self):
        return str(self.name)


class Tarok(Card):
    """Class for tarok cards

    The tarok cards do NOT have a rank precoded, it's recomended that you use
    rank 5. Allso the weigth for counting at the end of the game is applyed.
    """

    rank_list_tarok = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
        "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "IXX",
        "XX", "XXI", "XXII", ]

    # XXX do we really need a rank for Tarok card class
    def __init__(self, suit, rank):
        Card.__init__(self, suit, rank)
        self.name = "Tarok " + self.rank_list_tarok[self.rank - 1]
        self.__set_weight()

    def __set_weight(self):
        """Setting weigth for tarok cards"""

        if self.rank == 1 or self.rank == 21 or self.rank == 22:
            self.weight = 5
        else:
            self.weight = 1


class Suits(Card):
    """Class for suited cards

    The correct rank for the red and black numbers is applyed.
    Weight for counting in the end is allso apllyed.
    """

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

    def __set_weight(self):
        """Setting weight for suited cards"""

        if self.rank >= 5:
            self.weight = self.rank - 3
        else:
            self.weight = 1


class Deck:
    """The deck class is representing a card deck

    It creates a valid tarok game deck.
    """

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
        """Shuffles deck instance"""

        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self, players, cards_each):
        """It splits the deck

        and returns a list od Player and Talon instances
        """

        hand_list = []
        # XXX ugly
        talon = len(self.cards) - players * cards_each
        while len(self.cards) > talon:
            for player in range(1, players + 1):
                hand_list.append(Player(player))
                for n in range(cards_each):
                    hand_list[player - 1].cards = self.cards.pop()
        hand_list.append(Talon(self.cards))
        return hand_list


class Hand:
    """"""

    def __init__(self, cards=None):
        self.cards = cards

    def pop_card(self):
        """"""

        return self.cards.pop()

    def add_cards(self, number):
        """"""

        pass


class Player(Hand):
    """"""

    def __init__(self, number, cards=None):
        self.number = number
        self.cards = cards


class Talon(Hand):
    """"""
    def __init__(self, cards):
        Hand.__init__(self, cards)
