import unittest
from Deck import Deck
from Card import Card
from CPU import CPU

class TestCPUMethods(unittest.TestCase):
    def test_should_ask_for_hit(self):
        cpu = CPU(Deck())
        cpu.cards_dealt =[Card("spade", 1, True), Card("heart", 5, False)]

        self.assertEquals(cpu.should_ask_for_hit(), True);

if __name__ == '__main__':
    unittest.main()
