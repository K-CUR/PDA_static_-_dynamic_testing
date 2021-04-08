import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):

    def setUp(self):
        self.card1 = Card("hearts", 8)
        self.card2 = Card("spades", 6)
        self.card3 = Card("diamonds", 5)
        self.card4 = Card("diamonds", 1)

        self.card_game = CardGame()


# CARDS

    def test_card_has_suit(self):
        self.assertEqual("hearts", self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(6, self.card2.value)

# GAME

    def test_if_card_is_ace(self):
        result = self.card_game.check_for_ace(self.card4)
        self.assertEqual(True, result)

