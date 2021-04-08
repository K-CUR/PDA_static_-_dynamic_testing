import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):

    def setUp(self):
        self.card1 = Card("diamonds", 1)
        self.card2 = Card("diamonds", 5)
        self.cards = [self.card1, self.card2]

        # need to bring in CardGame class to setUp
        self.card_game = CardGame()


    def test_if_card_is_ace_true(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_if_card_is_ace_false(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 6", result)
