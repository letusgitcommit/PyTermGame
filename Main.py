"""
The Main application that will actually run the game.
"""

from Player import Entity
from Plots import get_encounters
from random import randint


def main():
    dragon = Entity('The Dragon')
    list_of_trials = get_encounters()

    welcome_text = '''
Welcome brave knight, to the quest to save the princess!
The kingdom needs you!
    
Sadly, your horse has run off with all of gear. 
You will have to find whatever tools you can along the way to help you defeat the dragon
'''
    print(welcome_text)

    knight = Entity(str(input('What is your name, brave knight? ')))

    text_after_name = '''
Thank you for braving the perils of this mountain, {username}.
You will start your adventure by entering the cave not too far from where we are here
    '''.format(username = knight.entity_name)
    print(text_after_name)

    for i in range(3):
        current_trial = list_of_trials.pop(randint(0,len(list_of_trials)-1))
        print(current_trial.trial_description())
        current_trial.get_choice_outcome(input('What shall you do adventurer? '))
        print('---------------------------------------------------------' , '', '')

main()

