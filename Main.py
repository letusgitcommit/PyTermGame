"""
The Main application that will actually run the game.
"""

from Player import Entity
from Plots import get_encounters
from random import randint
from Player_Item import Item
from Plot_Class import WrongChoice

def End_Game():
    print('You have died')
    end_game_choice = input('Do you want to retry? Y/N')
    if end_game_choice.lower() == 'y':
        main()
    else:
        exit()

def main():
    dragon = Entity('The Dragon')

    welcome_text = '''
Welcome brave knight, to the quest to save the princess!
The kingdom needs you!
    
Sadly, your horse has run off with all of your gear. 
You will have to find whatever tools you can along the way to help you defeat the dragon
'''
    print(welcome_text)

    knight = Entity(str(input('What is your name, brave knight? ')))
    print('\n\n', '---------------------------------', '\n\n')
    list_of_trials, battle = get_encounters(knight, dragon)
    text_after_name = '''
Thank you for braving the perils of this mountain, {username}.
You will start your adventure by entering the cave not too far from where we are here
    '''.format(username = knight.entity_name)
    print(text_after_name)

    def get_choice_encounter(knight):
        try:
            current_trial.get_choice_outcome(input('What shall you do adventurer? '), knight)
        except (ValueError, WrongChoice):
            print('Sorry, that what was a wrong choice. Please try again.')
            get_choice_encounter(knight)

    for i in range(3):
        current_trial = list_of_trials.pop(randint(0,len(list_of_trials)-1))
        print(current_trial.trial_description())
        get_choice_encounter(knight)


        print('---------------------------------------------------------' , '', '')
        if knight.health < 1:
            End_Game()
    print(battle.open_text)
    knight.inventory['Weapon'] = Item('Excalibur', 50, 0)
    while knight.health > 0 and dragon.health > 0:
        print(battle.battle_text)
        try:
            print(battle.battle_choice())
        except ValueError:
            print('Sorry, please enter 0 or 1.')
            print(battle.battle_choice())
        # Used in debugging
        # print('\n', 'Dragon health is {}'.format(dragon.health), '\n')
        # print('\n', 'Knight health is {}'.format(knight.health), '\n')
    if knight.health < 1:
        End_Game()
    else:
        print('Yay, you have killed the dragon!')
        exit()

main()

