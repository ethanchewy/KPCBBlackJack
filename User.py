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
        return self.sum > 21

    """Takes a card hit from the dealer

    Also, changes the sum and cards_dealt attributes according depending on what card is dealt

    :param user_type: the type of user that is getting the hit
    """
    def hit(self, user_type):
        card = self.deck.give_card(self)
        print(user_type + " draws a " + str(card.number) + " of " + card.suit)
        self.cards_dealt += [card]
        self.take_hit(card)


    """Process hit

    :param Card: Card that has just been dealt to the user
    """
    def take_hit(self, card):
        if card.is_ace:
            sums = [self.sum + 1, self.sum + 11]
            self.sum = min(sums, key = lambda s: self.sum - s)
        else:
            self.sum += card.number


    """Checks if user has a blackjack

    :rtype: boolean
    """
    def blackjack(self):
        return self.sum == 21
