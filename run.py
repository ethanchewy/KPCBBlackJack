from Card import Card
from User import User
from CPU import CPU
from Player import Player
from Deck import Deck

def restart_game():
    print("Do you want to continue? (Y/N)")
    response = input()

    while response != "Y" and response != "y" and response != "N" and response != "n":
        print("I don't understand your input. Please type Y or N for yes or No")
        print("Do you want to continue? (Y/N)")
        response = input()

    if response == "Y" or response == "y":
        return True
    else:
        return False

def main():
    print("Welcome to BlackJack!!")

    deck = Deck()
    player = Player(deck)
    cpu = CPU(deck)
    should_go = True

    def should_continue():
        print("Do you want to try again?")
        nonlocal deck
        nonlocal player
        nonlocal cpu
        if restart_game():
            deck = Deck()
            player = Player(deck)
            cpu = CPU(deck)
            return True
        else:
            return False

    while should_go:
        if cpu.is_done and player.is_done:
            print("CPU got: " + str(cpu.sum) + " You got: " + str(player.sum))
            if cpu.sum > player.sum:
                print("You lost!")
            elif cpu.sum == player.sum:
                print("You tied!")
            else:
                print("You won!")
            should_go = should_continue()
            continue

        player.ask_take_hit()
        if player.has_busted():
            print("You got " + str(player.sum) + " which is over 21. BUSTED!")
            print("You lost!")
            should_go = should_continue()
            continue

        if not cpu.is_done and cpu.should_ask_for_hit():
            cpu.hit("CPU")
        else:
            cpu.is_done = True

        if cpu.has_busted():
            print("CPU got " + str(cpu.sum) + " which is over 21. BUSTED!")
            print("You won!")
            should_go = should_continue()
            continue

        print("CPU has: " + str(cpu.sum) + " You have: " + str(player.sum))

        print()

    print("Thanks for playing!")


if __name__== "__main__":
    main()
