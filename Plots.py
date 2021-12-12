"""
This module will actually build out a list of encounters using the
Plot_class module
"""


from Plot_Class import Trial
from Player_Item import Item
from random import randint


class EndGame(Exception):
    print('You have escaped with your life, but left your dignity far behind')


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
    crossbow,
    m17,
    longsword,
    longsword,
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


def get_random_item():
    return List_of_Items[randint(0, len(List_of_Items) - 1)]


def get_damage():
    return randint(10, 50)


# Deprecated for the time being
# def do_nothing():
#     return None
#

#
# def exit_game():
#     raise EndGame


# I need to specify an integer to represent the outcome and use a trial class method to operate the function.
# These happen to all call their respective functions. Which is just prefilling the list and exiting the game.
dict_of_settings_and_choice_outcomes = {
    'a cold, wet, cobblestone room': [2, 3, 3],
    'the mouth of another cave, full of stalagmites and stalactites': [2, 1, 3],
    'a bare room made of pure white marble brick, unmarred by the passage of time': [1, 2, 3],
    'a torch lit dungeon cell, full of seemingly harmless multi-colored bubbles made of rubber': [3, 3, 3],
    'the bottom of a fissure opened to the sky, with a bridge in front of you, running across a river of lava': [1, 2, 3]
}

list_of_feelings = [
    'Happy',
    'Sad',
    'Angry',
    'Bored',
    'Hot',
                    ]

list_of_sounds = ['the claws of a tremendous and terrible beast scraping upon stone',
                  'something like the breaking of a wire',
                  'deafening silence',
                  'the roar of a dragon',
                  'the scream of a maiden in distress']

list_of_choices = ['Investigate Further...', 'Move On.', 'Escape as quickly as possible, yellow bellied coward!']


def get_encounters():
    LIST_OF_TRIALS = []
    for key in dict_of_settings_and_choice_outcomes.keys():
        LIST_OF_TRIALS.append(Trial('placeholder',
                                    key,
                                    list_of_feelings[randint(0, len(list_of_feelings)- 1)],
                                    list_of_sounds[randint(0, len(list_of_sounds)-1)],
                                    list_of_choices,
                                    dict_of_settings_and_choice_outcomes[key]),
                                    get_damage(),
                                    get_random_item()
                              )
    return LIST_OF_TRIALS

