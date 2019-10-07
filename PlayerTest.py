import unittest
from Deck import Deck
from Player import Player

class TestCPUMethods(unittest.TestCase):
    def test_should_ask_for_hit(self):
        player = Player(Deck())

        self.assertIsNone(player.ask_take_hit(), True);

if __name__ == '__main__':
    unittest.main()
