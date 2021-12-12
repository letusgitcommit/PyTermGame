"""
This will be the module that will allow our knight to pass through the
trials of our dungeon.
"""

class Wrong_Choice(Exception):
    return "You did not pick a valid option!"

class Trial:
    def __init__(self, name, trial_text, pot_damage, pot_item):
        self.name = name
        self.trial_text = trial_text
        self.pot_damage = pot_damage
        self.pot_item = pot_item


    def __repr__(self):
        return self.name

    def trial_description(self):
        return self.trial_text

    def grant_damage(self):
        return self.pot_damage

    def grant_item(self):
        return self.pot_item

    def grant_nothing(self):
        return None

    def chosen(self, choice):
        if choice == 1:
            return self.grant_damage()
        elif choice == 2:
            return self.grant_item()
        elif choice == 3:
            return self.grant_nothing()
        else:
            raise Wrong_Choice

