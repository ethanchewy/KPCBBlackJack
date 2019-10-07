import unittest
from Card import Card

class TestUserMethods(unittest.TestCase):
    def test_constructor(self):
        card = Card("test", 1, False)

if __name__ == '__main__':
    unittest.main()
