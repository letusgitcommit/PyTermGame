"""
This is going to be the player class module.
This class should track the player's stats, inventory, along with actions
that the player can take on any given turn.
"""

# We import the random module to handle attack and defense calculations
from random import randint


class Player:

    def __init__(self, player_name):
        """This class will be used to instantiate the player for use throughout the game"""
        self.player_name = player_name
        # The inventory will contain items that can be used to attack,
        # defend, and heal oneself
        self.inventory = {}
        # At this time, we can just track health with a counter
        self.health = 100
        # Armor and Attack will hold two integers that track the range that we can
        # pull from to calculate the randint range
        # self.armor = []
        # self.attack = []
        # commented out due to the choice to calculate attack and defense
        # based on items in inventory

    def calculate_attack(self):
        pass
