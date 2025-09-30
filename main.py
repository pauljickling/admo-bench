import random

# set to true if using Into-theOdd style autohits
AUTOHIT = False

party = []


class PlayerCharacter:
    def __init__(self, name, level=1, hp=0, ac=None, tohit=0, damage=(1, 6)):
        self.name = name
        self.level = level
        self.hp = hp if hp != 0 else level * 4
        self.ac = ac if ac is not None else (0 if AUTOHIT else 10)
        self.tohit = tohit
        self.damage = damage

    def __str__(self):
        return (f"PlayerCharacter(name='{self.name}', level={self.level}, "
                f"hp={self.hp}, ac={self.ac}, tohit={self.tohit}, "
                f"damage={self.damage})")

class Monster:
    def __init__(self, name, hd=1, ac=None, damage=(1, 6), morale=7):
        self.name = name
        self.hd = hd
        self.hp = hd * 4
        self.ac = ac if ac is not None else (0 if AUTOHIT else 10)
        self.tohit = hd
        self.damage = damage
        self.morale = morale

    def __str__(self):
        return (f"Monster(name='{self.name}', hd={self.hd}, "
                f"hp={self.hp}, ac={self.ac}, tohit={self.tohit}, "
                f"damage={self.damage}, morale={self.morale})")
