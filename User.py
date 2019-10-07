class User:

    """Initialize the User object

    :param self: whatever initialized and creatd this user object
    :param deck: deck of cards associated with the user
    """
    def __init__(self, deck):
        self.is_done = False
        self.sum = 0
        self.cards_dealt = []
        self.deck = deck

    """Returns if the sum of the user's current cards is over 21

    :rtype: boolean
    """
    def has_busted(self):
        return sum > 21

    """Takes a card hit from the dealer

    Also, changes the sum and cardsDealt attributes according depending on what card is dealt
    """
    def hit(self):
        card = self.deck.give_card(self)


    """Process hit

    :param Card: Card that has just been dealt to the user
    """
    def take_hit(self, card):
        if card.isAce:
            sums = [self.sum + card.number[0], self.sum + card.number[1]]
            self.sum = min(sums, key = lambda s: self.sum - s)
        else:
            self.sum += card.number


    """Checks if user has a blackjack

    :rtype: boolean
    """
    def blackjack(self):
        return self.sum == 21


