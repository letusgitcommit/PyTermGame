"""
This module will actually build out a list of encounters using the
Plot_class module
"""

import Plot_Class
from Player_Item import Item

from random import randint

mjolnir = Item('Mjolnir, Hammer of Thor', 10)
wooden_stick = Item('A Wooden Stick', 0)
crossbow = Item('A crossbow with some bolts', 3)
m17 = Item('A Sig P320 M17, 9mm, mint condition with a fully loaded magazine of hollow point bullets', 1)
longsword = Item('A steel longsword', 3)
staff_of_power = Item('A long ebony staff, crackling with electrical charge', 100)
dagger = Item('A small rusty dagger', 1)
pickaxe = Item('A well oiled pickaxe in suitable condition', 2)
iron_shield = Item('An iron shield crested with a griffon', 2)
plate_armor = Item('A full set of plate armor', 5)
fancy_clothes = Item('Some fancy clothes, with a barf stain', 0)
sun_glasses = Item('Secret Agent sun glasses, complete with ear piece, used to stylishly conceal your identity', 0)
bear_skin = Item('A tattered bear skin turned cloak', 0)
diamond_armor = Item('May Notch guide you and keep you', 100)
health_potion1 = Item('Health Potion', 1)
health_potion2 = Item('Health Potion', 2)
health_potion4 = Item('Health Potion', 4)
health_potion10 = Item('Health Potion', 10)

List_of_Items = [
    mjolnir,
    wooden_stick,
    wooden_stick,
    wooden_stick,
    crossbow,
    crossbow
    m17,
    longsword,
    longsword
    staff_of_power,
    dagger,
    dagger,
    dagger,
    pickaxe,
    iron_shield,
    iron_shield,
    iron_shield,
    plate_armor,
    fancy_clothes,
    fancy_clothes,
    sun_glasses,
    bear_skin,
    diamond_armor,
    health_potion1,
    health_potion1,
    health_potion2,
    health_potion2,
    health_potion4,
    health_potion10
]




dict_of_settings_and_choice_outcomes = ['a cold, wet, cobblestone room',
                    'the mouth of another cave, full of stalagmites and stalactites',
                    'a bare room made of pure white marble brick, unmarred by the passage of time',
                    'a torch lit dungeon cell, full of seemingly harmless multi-colored bubbles made of rubber',
                    'the bottom of a fissure opened to the sky, with a bridge in front of running across a river of lava']

list_of_feelings = ['Happy',
                    'Sad',
                    'Angry',
                    'Bored',
                    'Hot',
                    ]

list_of_sounds = ['the claws of a tremendous and terrible beast scraping upon stone',
                  'something like the breaking of a wire',
                  'deafening silence',
                  'the roar of a dragon'
                  'the scream of a maiden in distress']

list_of_choices['Investigate Further...', 'Move On.', 'Escape as quickly as possible, yellow bellied coward!']


