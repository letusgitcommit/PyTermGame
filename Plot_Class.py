"""
This will be the module that will allow our knight to pass through the
trials of our dungeon.
"""


class WrongChoice(Exception):
    pass


class Trial:
    def __init__(self, name, setting, feeling, sound, choices, choice_outcomes, pot_damage, pot_item):
        self.name = name
        self.setting = setting
        self.feeling = feeling
        self.sound = sound
        self.choices = choices
        self.choice_outcomes = choice_outcomes
        self.pot_damage = pot_damage
        self.pot_item = pot_item


    def __repr__(self):
        return self.name

    def trial_description(self):
        trial_text = '''
You encounter {setting}.
You feel {feeling}.
You hear {sound}.\n\n'''.format(    setting = self.setting,
                                    feeling = self.feeling,
                                    sound = self.sound)

        trial_text += 'You have {} choices. \n\n'.format(len(self.choices))
        for choice in self.choices:
            trial_text += 'Choice {choice_number}: {choice_text} \n'.format(choice_number
                                                                         = (self.choices.index(choice) + 1),
                                                                         choice_text = choice)
        return trial_text

    def get_choice_outcome(self, choice_int, entity):
        if int(choice_int) not in range(1,5):
            raise WrongChoice
        self.chosen(int(choice_int), entity)

    def grant_damage(self, entity):
        entity.calculate_damage_taken(self.pot_damage)
        return 'You have received {} points of damage'.format(self.pot_damage)

    def grant_item(self, entity):
        entity.add_to_inventory(self.pot_item, self.pot_item.item_type)
        return 'You have received {}'.format(self.pot_item.name)

    def grant_nothing(self, entity):
        return '{}, nothing has happened...'.format(entity.entity_name)

    def print_newlines(self, text):
        print('\n', '--------------', text, '--------------','\n')

    def chosen(self, choice, entity):
        if int(choice) < len(self.choice_outcomes) + 1:
            choice_option = int(self.choice_outcomes[int(choice) - 1])
        else:
            choice_option = int(choice)
        if choice_option == 1:
            self.print_newlines(self.grant_damage(entity))
        elif choice_option == 2:
            self.print_newlines(self.grant_item(entity))
        elif choice_option == 3:
            self.print_newlines(self.grant_nothing(entity))
        elif choice_option == 4:
            self.print_newlines(entity.check_inventory())
            next_choice = input('What\'s your next move? ')
            self.get_choice_outcome(next_choice, entity)
        else:
            raise WrongChoice


class Battle:

    list_of_options = ['Smite the dragon with your weapon',
                       'Drink your health potion to regain your battle stamina']

    def __init__(self, knight, dragon):
        self.open_text = 'Gasp! You have come upon the dragon in his lair'
        self.battle_text = self.present_battle_options()
        self.knight = knight
        self.dragon = dragon


    def present_battle_options(self):
        message_text = ''
        for option in self.list_of_options:
            message_text += 'Choice {}: {} \n'.format(self.list_of_options.index(option), option)
        return message_text

    def battle_choice(self):
        choice = int(input('What shall you choose? '))
        if choice in range(0, 2):
            if choice == 0:
                message_text = '\n\n'
                damage, attack_text = self.knight.attack()
                self.dragon.calculate_damage_taken(damage)
                message_text += attack_text + '\n'
                message_text += self.dragon.random_action_dragon(self.knight) + '\n'
                return message_text
            else:
                message_text = '\n\n'
                message_text += self.knight.heal()
                message_text += '\n\n'
                message_text += self.dragon.random_action_dragon(self.knight) + '\n\n'
                return message_text
        else:
            return '\n', 'Please choose 0 or 1.', '\n'
