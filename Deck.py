import random
from Card import Card

class Deck:

    """Initializes a Deck object

    :param self: whatever initialized and created this deck object
    """
    def __init__(self):
        self.cards = self.generate_random_deck()

    """Gives user the top card of the deck

    :param user: the user asking for the hit
    :rtype: Card
    """
    def give_card(self, user):
        return self.cards.pop()

    """Generate a set of 52 cards

    :rtype: Card[]
    """
    def generate_random_deck(self):
        cards = []
        for num in range(1, 14):
            num_added = num
            if num >= 10:
                num_added = 10
            for suit in ["spade", "heart", "club", "diamond"]:
                cards += [Card(suit, num_added, num==1)]

        random.shuffle(cards)

        return cards

    """Reset deck
    """
    def reset(self):
       self.cards = self.generate_random_deck()
