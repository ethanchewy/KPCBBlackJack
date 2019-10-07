class Card:

    """Initializes the Card object

    :param self: whatever initialized and creatd this card object
    :param suit: spade, heart, club, or diamond
    :param number: number value of the card
    :param is_ace: indicates if the card is an ace or not
    """
    def __init__(self, suit, number, is_ace):
        self.suit = suit
        self.number = number
        self.is_ace = is_ace
