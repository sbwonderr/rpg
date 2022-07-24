import sys
from random import randint
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


def print_jet(text):
    for c in text:
        print('\033[94m' + c + '\033[0m', end="")
        sys.stdout.flush()
        sleep(0.05)
    print("")


class Character:  # Overall character architecture, may need to add more for enemies
    def __init__(self, name, hp, exp):
        self.name = name
        self.hp = hp
        self.exp = exp


player_name = input("...my name is... ")
inventory = ["strange medallion"]


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
            "c": lambda: player.status(player1),
            "e": lambda: Room.searchitem(itemroom)}  # input commands directory #TODO: add more as needed


def get_input(commands):  # input loop for player commands
    while True:
        user_entered = input()  # unprompted input
        if user_entered not in commands:  # loop for incorrect input
            print("No. Press c for status, press i for inventory")
            user_entered = None  # clears input
        else:
            return commands[user_entered]()  # calls request from commands directory


class Room:
    def __init__(self, name="room", description="room", enemy=None):
        if enemy is None:
            enemy = []
        self.name = name
        self.description = description
        self.enemy = enemy

    def searchitem(self):
        roomitems_all = ["potion", "gold", "dinner"]
        lootroll = randint(0, 99)
        if lootroll >= 49:
            randitem = roomitems_all[randint(0, 2)]
            print(randitem)
            inventory.append(randitem)
            print("inventory is now ", end='')
            print(inventory)
        else:
            print("No items were found")

    def printroom(self):
        print("Name: {}, description: {}, enemy:{}\n".format(
            self.name, self.description, self.enemy))

enemyroom = Room("ROOM", "room", "goblin") #define a room
itemroom = Room("item room", "empty room with a chest", [])
restroom = Room("rest room", "nothing's here, looks like a good place to rest", [])

player.status(player1) #test player status print
Room.printroom(restroom) #test room print, name, descrip, enemy
Room.searchitem(itemroom) #test search room for item
get_input(commands) #test player input for any command


