"""
This will be the module that will allow our knight to pass through the
trials of our dungeon.
"""


class WrongChoice(Exception):
    print("You did not pick a valid option!")


class Trial:
    def __init__(self, name, setting, feeling, sound, choices, choice_outcomes, pot_damage=0, pot_item=None):
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
        trial_text = '''You encounter {setting}. \n
                        You feel {feeling}. \n
                        You hear {sound}. \n'''.format( setting = self.setting,
                                                        feeling = self.feeling,
                                                        sound = self.sound)
        trial_text += 'You have {} choices. \n'.format(len(self.choices))
        for choice in self.choices:
            trial_text += 'Choice {choice_number}: {choice_text} \n'.format(choice_number
                                                                         = (self.choices.index(choice) + 1),
                                                                         choice_text = choice)
        return trial_text

    def get_choice_outcome(self, choice_int):
        if choice_int not in range(1,4):
            raise WrongChoice
        return self.choice_outcomes[choice_int - 1]

    # Deprecated for the time being
    # def grant_damage(self):
    #     return self.pot_damage
    #
    # def grant_item(self):
    #     return self.pot_item
    #
    # def grant_nothing(self):
    #     return None

    # Deprecated for the time being
    # def chosen(self, choice):
    #     if choice == 1:
    #         return self.grant_damage()
    #     elif choice == 2:
    #         return self.grant_item()
    #     elif choice == 3:
    #         return self.grant_nothing()
    #     else:
    #         raise Wrong_Choice

