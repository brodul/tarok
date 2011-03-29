from deck import *

def deal(deck):
    """ Return a list, card for players are in a list. The last list is talon.
    """
    list =[]
    for player in range(4):
        list.append(deck[player*12: (player+1)*12])
    list.append(deck[48:])
    return list

deck = Deck()
print deck.cards
print deck

