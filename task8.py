"""task8"""

import random


class Hero:
    """
    description
    """
    def __init__(self, hero_num, hero_feature, level):
        self.hero_num = hero_num
        self.hero_feature = hero_feature
        self.level = level

    def level_up(self):
        """
        description
        """
        my_level = self.level + 1
        self.level = my_level
        return self.level


class Solder:
    """
    description
    """
    def __init__(self, solder_num, solder_feature):
        """
        description
        """
        self.solder_num = solder_num
        self.solder_feature = solder_feature

    @staticmethod
    def move_to_hero(hero_obj):
        """
        description
        """
        return hero_obj


def a_game():
    """
    description
    """
    first_hero = Hero(1, 1, 1)
    # first_solder = Solder(1, 1)
    random_val = random.randrange(1, 10)

    teams_solder: list = [first_hero, first_hero]
    for _ in range(random_val):
        random_team = random.randrange(1, 3)
        new_solder = Solder(1, random_team)
        print(new_solder.solder_num)
        teams_solder.append(teams_solder)
    team_1_count = 0
    team_2_count = 0
    for solder_is in teams_solder:
        if solder_is.hero_feature == 1:
            team_1_count += 1
        else:
            team_2_count += 1
    print(team_1_count)
    print(team_2_count)
    if team_1_count > team_2_count:
        first_hero.level_up()
    return print(first_hero.hero_num)


a_game()
