import random

import unittest

import deck as deck

TAROK_NUM = 22


class TestTarokCreation(unittest.TestCase):
    
    def setUp(self):
        self.last_num = TAROK_NUM - 1
    
    def test_last_tarok(self):
        self.last_tarok = deck.Tarok(4, self.last_num)
        self.assertEqual(repr(self.last_tarok), "Tarok XXII")

    def test_outofrange(self):
        self.assertRaises(IndexError, deck.Tarok, 4, TAROK_NUM)


class TestSuitsCreation(unittest.TestCase):

    def test_red_suit(self):
        self.red = deck.Suits(0, 2)
        self.assertEqual(repr(self.red), "2 of Diamonds")

    def test_black_suit(self):
        self.black = deck.Suits(3, 2)
        self.assertEqual(repr(self.black), "9 of Clubs")

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck1 = deck.Deck()

    def test_shuffle(self):
        self.deck1.shuffle()

