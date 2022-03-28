class Monster:
    def __init__(self, name, strength, age, canFly=False, weapon=None):
        self.name = name
        self.strength = strength
        self.age = age
        self.canFly = canFly
        self.weapon = weapon


class Dragon(Monster):
    def __init__(self, name, strength, age):
        super().__init__(name, strength, age, True, "Fire")

class Ogre(Monster):
    def __init__(self, name, strength, age, weapon=None):
        super().__init__(name, strength, age, False, weapon)

class Dinosaur(Monster):
    def __init__(self, name, strength, age, canFly=False):
        super().__init__(name, strength, age, canFly, "Punch")