# text speed settings
import sys
from time import sleep


def print_slowly(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(1)
    print("")


def print_speech(text):
    for c in text:
        print(c, end="")
        sys.stdout.flush()
        sleep(0.05)
    print("")


# intro text
print_slowly('LOADING')
print_speech("Hey stranger, you feeling alright?")
print_slowly('...')
print_speech("Whoa hey, slow it down. You got a little banged up in the crash. What were you flying anyways?")
print_slowly('...')
print_speech("Okay, you don't know, that's cool. One step at a time. What's your name, kid?")
# name definition
player_name = input("...my name is... ")

print_speech(player_name + ", huh? That's quite the name. Sounds powerful, like an old legend.")
print_speech("My name's " + '\033[94m'"Jet"'\033[0m' + ". Glad to make your acquaintance.")


# Jet character text settings
def print_jet(text):
    for c in text:
        print('\033[94m' + c + '\033[0m', end="")
        sys.stdout.flush()
        sleep(0.05)
    print("")


print_jet("Anyways, I noticed something in the wreck that looked important. I threw it in this bag, keep it.")

# inventory
inventory = ["strange medallion"]
player_input = input("Press i to open inventory\n")
while player_input != "i":
    print("No")
    player_input = None
    # noinspection PyRedeclaration
    player_input = input("Press i to open inventory\n")
else:
    print(inventory)

# more intro text
print_jet("Not sure what it is, hopefully you can make some sense of it.")
print_jet("Take your time getting up, no rush. Make sure you have all your body parts.")


# status screen

class Character:  # Overall character architecture, may need to add more for enemies
    def __init__(self, name, hp, exp):
        self.name = name
        self.hp = hp
        self.exp = exp


class player(Character):  # player character stats
    exp = 0
    hp = 10
    name = player_name

    def __init__(self, hp, exp):
        super().__init__(player_name, hp, exp)

    def status(self): print("Name: {}, HP: {}, XP:{}\n".format(
        player.name, player.hp, player.exp))  # returns player stats, printed nicely


player1 = player(10, 0)  # base states for player character
commands = {"i": lambda: print(inventory),
            "c": lambda: player.status(player1)}  # input commands directory #TODO: add more as needed


def get_input(commands):  # input loop for player commands
    while True:
        user_entered = input()  # unprompted input
        if user_entered not in commands:  # loop for incorrect input
            print("No. Press c for status, press i for inventory")
            user_entered = None  # clears input
        else:
            return commands[user_entered]()  # calls request from commands directory


# back to tutorial
player_input = input("Press c for character info\n")
while player_input != "c":  # question repeats until c is pressed
    print("No")
    player_input = None  # clears player input for reevaluation
    # noinspection PyRedeclaration
    player_input = input("Press c for character info\n")  # repeats prompt
else:
    commands["c"]()  # returns status

get_input(commands)  # Waiting for free roam loop

# TODO: Package commands into separate module
# TODO: Nest tutorial fragments into own loop
# Done for inventory, status
# TODO:Set up free roam loop
