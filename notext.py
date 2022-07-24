import numpy as np
from random import *

class Building:
    """A Building is filled with Rooms.
    reqitems: a list of items that must go into the building before procedural generation finishes.
    reqenemies: a list of enemies that must go into the building before procedural generation finishes.
    reqpeople: a list of people that must go into the building before procedural generation finishes.
    isgridshaped: a True/False value indicating whether this building should be grid-shaped.
    map: a Numpy array of Rooms.
    """
    # TODO: Accommodate non-grid-shaped buildings
    def __init__(self, reqitems, reqenemies, reqpeople, isgridshaped):
        self.reqitems = reqitems
        self.reqenemies = reqenemies
        self.reqpeople = reqpeople
        self.isgridshaped = isgridshaped
        if isgridshaped:    # Set limits on how far n/s/w/e/up/down from the starting room Rooms are allowed to go.
            self.limit_north = 3
            self.limit_south = 3
            self.limit_west = 3
            self.limit_east = 3
            self.limit_up = 3
            self.limit_down = 3
        else:   # If the building is not grid-shaped, then there are no such limits.
            self.limit_north = None
            self.limit_south = None
            self.limit_west = None
            self.limit_east = None
            self.limit_up = None
            self.limit_down = None
        self.map = np.array([[[]]])     # TODO: Put a room here


class Room:
    """Generic room class.
    transitions: a list of transitions, such as ["n", "s", "w", "e", "up", "down"]
    """
    def __init__(self, name="room", description="room", enemy=None, transitions=None):
        if enemy is None:
            enemy = []
        if transitions is None:
            transitions = []
        self.name = name
        self.description = description
        self.enemy = enemy
        self.transitions = transitions

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



laboratory = Building(["potion"], ["gobbo"], ["lady"], True)
