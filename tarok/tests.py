import random

import unittest

import deck as deck
import end as end

TAROK_NUM = 22


class TestTarokCreation(unittest.TestCase):

    def setUp(self):
        self.last_num = TAROK_NUM

    def test_last_tarok(self):
        self.last_tarok = deck.Tarok(4, self.last_num)
        self.assertEqual(repr(self.last_tarok), "Tarok XXII")

    def test_outofrange(self):
        self.assertRaises(IndexError, deck.Tarok, 4, TAROK_NUM + 1)


class TestSuitsCreation(unittest.TestCase):

    def test_red_suit(self):
        self.red = deck.Suits(1, 3)
        self.assertEqual(repr(self.red), "2 of Diamonds")

    def test_black_suit(self):
        self.black = deck.Suits(4, 3)
        self.assertEqual(repr(self.black), "9 of Clubs")


class TestCardComparison(unittest.TestCase):

    def setUp(self):
        self.lower = deck.Suits(3, 5)
        self.lower2 = deck.Suits(1, 5)
        self.higher = deck.Suits(2, 6)
        self.tarok = deck.Tarok(5, 1)

    def test_equal(self):
        self.assertRaises(Exception, self.lower.__cmp__, self.lower)
        self.assertRaises(Exception, self.higher.__cmp__, self.higher)
        self.assertRaises(Exception, self.tarok.__cmp__, self.tarok)

    def test_equal_rank(self):
        self.assertTrue(self.lower == self.lower2)

    def test_not_equal(self):
        self.assertNotEqual(self.lower, self.higher)
        self.assertNotEqual(self.higher, self.tarok)
        self.assertNotEqual(self.tarok, self.lower)

    def test_self_greater(self):
        self.assertTrue(self.higher > self.lower)
        self.assertTrue(self.tarok > self.lower)


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck1 = deck.Deck()

    def test_shuffle(self):
        self.deck1.shuffle()


class TestCount(unittest.TestCase):

    def setUp(self):
        self.deck = deck.Deck()
        self.discard = end.Discard()
        self.example = [deck.Suits(1, 1), deck.Suits(1, 2), deck.Suits(1, 3),
                        deck.Tarok(5, 1), deck.Suits(4, 8)]

    def test_count_deck(self):
        self.discard.cards = self.deck.cards
        self.assertEqual(self.discard.count(), 70)

    def test_count_two_cards(self):
        self.discard.cards = self.example[2:]
        self.assertEqual(self.discard.count(), 9)

    def test_count_five_cards(self):
        self.discard.cards = self.example
        self.assertEqual(self.discard.count(), 10)
