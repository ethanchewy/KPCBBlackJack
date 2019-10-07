import unittest
from User import User
from Deck import Deck
from Card import Card

class TestUserMethods(unittest.TestCase):
    def test_busted(self):
        user = User(Deck())
        user.sum = 0
        self.assertEqual(user.has_busted(), False)
        user.sum = 50
        self.assertEqual(user.has_busted(), True)

    def test_hit(self):
        user = User(Deck())
        self.assertIsNone(user.hit("asdfasdf"))

    def test_split(self):
        user = User(Deck())
        self.assertIsNone(user.take_hit(Card("asdf", 1, False)))

if __name__ == '__main__':
    unittest.main()
