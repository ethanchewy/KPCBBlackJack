import unittest
from Deck import Deck
from Card import Card
from User import User

class TestUserMethods(unittest.TestCase):
    def test_give_card(self):
        deck = Deck()
        user = User(deck)
        self.assertIsInstance(deck.give_card(user), Card)

    def test_generate_random_deck(self):
        deck = Deck()
        self.assertEquals(len(deck.cards), 52)

    def test_reset(self):
        deck = Deck()
        deck.reset()
        self.assertEquals(len(deck.cards), 52)

if __name__ == '__main__':
    unittest.main()
