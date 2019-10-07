from User import User
class Player(User):

    """Initialize the Player Object

    :param self: whatever initialized and creatd this Player object
    """
    def __init__(self, deck):
        super().__init__(deck)

    """Ask player if it wants a hit
    """
    def ask_take_hit(self):
        answer = None
        print("Do you want a hit (Y/N)?")
        answer = input()

        while answer != "Y" and answer != "N" and answer != "y" and answer != "n":
            print("I don't understand your input. Please type Y or N for yes or No")
            print("Do you want a hit (Y/N)?")
            answer = input()

        if answer == "Y" or answer == "y":
            self.hit("You")
        else:
            self.is_done = True





