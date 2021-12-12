"""
We will use this module to create the classes and possible items that a
player can obtain on their journey.
I think currently, we can have three items, weapon, shield, and health
potion
"""

# We will use random to calculate item stats
from random import randint


class Item:
    """This will be the base class for constructing our items, whether weapon, armor, or health potion"""
    def __init__(self, name, item_class, item_type):
        self.item_types = ['Weapon', 'Armor', 'Health Potion']
        # We can create some fun weapon names and not reveal their stats
        self.name = name
        # The item class will determine the efficacy of the item
        # Should be an integer
        self.item_class = item_class
        self.item_type = self.item_types[item_type]

    def __repr__(self):
        return self.name

    def calculate_efficacy(self):
        return randint(0, self.item_class * 10) + self.item_class
