"""
This is going to be the Entity class module.
This class should track the Entity's stats, inventory, along with actions
that the Entity can take on any given turn.
We can use this for the dragon and the player.
"""

# We import the random module to handle dragon actions
from random import randint

from Player_Item import Item


class Entity:

    def __init__(self, entity_name):
        """This class will be used to instantiate the Entity for use throughout the game"""
        self.entity_name = entity_name
        # The inventory will contain items that can be used to attack,
        # defend, and heal oneself
        self.inventory = {'Weapon': None, 'Armor': None, 'Health Potion': None}
        # At this time, we can just track health with a counter
        self.health = 100
        if entity_name == 'The Dragon':
            self.health += 100
            self.inventory['Weapon'] = Item('Flaming Breath', 5, 0)
            self.inventory['Armor'] = Item('Dragon Scale', 5, 1)
            self.inventory['Health Potion'] = Item('Shed Skin', 5, 2)
        # Armor and Attack will hold two integers that track the range that we can
        # pull from to calculate the randint range
        # self.armor = []
        # self.attack = []
        # commented out due to the choice to calculate attack and defense
        # based on items in inventory

    def get_efficacy(self, item):
        try:
            return item.calculate_efficacy()
        except:
            return 1

    def calculate_attack(self):
        weapon = self.inventory.get('Weapon')
        return self.get_efficacy(weapon)

    def calculate_defense(self):
        armor = self.inventory.get('Armor')
        return self.get_efficacy(armor)

    def calculate_hp(self):
        health_potion = self.inventory.get('Health Potion')
        self.inventory['Health Potion'] = None
        if health_potion != None:
            return self.get_efficacy(health_potion)
        else:
            return 1

    def add_to_inventory(self, item, item_type):
        self.inventory[item_type] = item

    def calculate_damage_taken(self, damage):
        total_damage = damage - self.calculate_defense()
        if total_damage > 0:
            total_damage = 0
        self.health -= total_damage
        return '{} has taken {} points of damage'.format(self.entity_name, total_damage)

    def heal(self):
        change_in_health = self.calculate_hp()
        self.health += change_in_health
        message = '{} has added {} to their health'.format(self.entity_name, change_in_health)
        return self.health, message

    def attack(self):
        attack_damage = self.calculate_attack()
        message = 'Huzzah! You have dealt {} points of damage'.format(attack_damage)
        return attack_damage, message

    def check_inventory(self):
        message_text = ''
        message_text += 'You have the following Items in your inventory: '
        message_text += str(self.inventory)
        return message_text

    def random_action_dragon(self, knight):
        action = randint(1, 3)
        if action == 1:
            return self.heal()
        if action == 2:
            return  knight.calaculate_damage_taken(self.attack())
        if action == 3:
            return "The ground quakes as the dragon roars"



