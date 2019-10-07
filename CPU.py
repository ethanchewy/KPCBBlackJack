from itertools import combinations
from User import User

class CPU(User):

    """Initialize the CPU object

    :param self: whatever initialized and created this CPU object
    """
    def __init__(self, deck):
        super().__init__(deck)
        self.sums = []

    """If all possibilities of the sum - 5 < 10, take the risk and take a hit.
    If not, do not take a hit and wait for the end of the game.

    :rtype: boolean
    """
    def should_ask_for_hit(self):
        aces = []
        aces_counter = 0
        without_aces = []

        for card in self.cards_dealt:
            if card.is_ace:
                aces += [1, 11]
                aces_counter += 1
            else:
                without_aces += [card.number]

        if aces_counter > 1:
            combos = combinations(aces, aces_counter)
            sums = []
            for combo in combos:
                sums += sum(without_aces + list(combo))
            return (min(sums) - 5) < 10
        elif aces_counter == 1:
            return (min(sum(without_aces) + 1, sum(without_aces) + 11) - 5) < 10

        return self.sum - 5 < 10
