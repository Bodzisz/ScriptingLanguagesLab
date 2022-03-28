import random

class Monster:
    name = "MONSTER"

    def __init__(self, name, strength, age, canFly=False, weapon=None):
        self.name = name
        self.strength = strength
        self.age = age
        self.canFly = canFly
        self.weapon = weapon

    def attack(self):
        print("%s atacks with %s [%s]" % (self.name, self.weapon, self.strength))
        return self.strength
    
    def move(self):
        raise NotImplementedError()

    def isFlier(self):
        return self.canFly


class Dragon(Monster):
    def __init__(self, name, strength, age):
        super().__init__(name, strength, age, True, "Fire")

    def move(self):
        print("Dragon ", self.name, " flies ...")

class Ogre(Monster):
    def __init__(self, name, strength, age, weapon="Punch"):
        super().__init__(name, strength, age, False, weapon)

    def move(self):
        print("Ogre ", self.name, " moves slowly on the ground ...")

class Dinosaur(Monster):
    def __init__(self, name, strength, age, canFly=False):
        super().__init__(name, strength, age, canFly, "Punch")

    def move(self):
        print("Dinosaur ", self.name, " moves fast on the ground ...")

class Game:
    def __init__(self, level=0):
        self.level = level
        self.playerMonster = None
        self.compMonster = None

    def printMainMenu(self):
        print("1. Start Game")
        print("2. Set level")
        print("3. Quit")

    def takeInput(self, text):
        return input(text)
    
    def start(self):
        exit = False
        while not exit:
            self.printMainMenu()
            choice = self.takeInput("Choice: ")
            if choice == '1':
                self.chooseCharacter()
                print("Press enter to start fight")
                input()
                self.fight()
                exit = True
            elif choice == '2':
                pass
            else:
                exit = True

    def getRandomMonster(self, monsterNumber, name):
        if monsterNumber == 1:
            return Dragon(name, random.randint(0,100), random.randint(0,100))
        elif monsterNumber == 2:
            return Ogre(name, random.randint(0,100), random.randint(0,100))
        else:
            return Dinosaur(name, random.randint(0,100), random.randint(0,100))
    
    def chooseCharacter(self):
        print("Choose charachter:")
        print("1. Dragon")
        print("2. Ogre")
        print("3. Dinosaur")
        choice = self.takeInput("Choice: ")
        if choice == '1':
            self.playerMonster = self.getRandomMonster(1, "myDragon")
        elif choice == '2':
            self.playerMonster = self.getRandomMonster(2, "myOgre")
        else:
            self.playerMonster = self.getRandomMonster(3, "myDinosaur")
        self.compMonster = self.getRandomMonster(random.randint(1,3), "EnemyName")

    def fight(self):
        print("Fight starts!!!")
        plStrength = self.playerMonster.attack()
        compStrength = self.compMonster.attack()
        if plStrength > compStrength:
            print("PLAYER WON!")
        elif plStrength < compStrength:
            print("PLAYER LOST!")
        else:
            print("BOTH MONSTERS DIED!")



# silverDragon = Dragon("silver", 21, 10)
# silverDragon.attack()
# silverDragon.move()
# print(silverDragon.isFlier())
game = Game()
game.start()