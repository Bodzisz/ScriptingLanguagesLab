from unicodedata import name


class Animal:
    def __init__(self, name, age, canFly=False, canSwim=False, color=None) -> None:
        self.name = name
        self.age = age
        self.canFly = canFly
        self.canSwim = canSwim
        self.color = color

    def isSwimmer(self):
        return self.canSwim

    def makeSound(self):
        raise NotImplementedError()

class Bird(Animal):
    def __init__(self, name, age, color=None) -> None:
        super().__init__(name, age, True, color)

    def makeSound(self):
        print("Cwir Cwir")

class LandAnimal(Animal):
    def __init__(self, name, age, canSwim=False, color=None) -> None:
        super().__init__(name, age, False, canSwim, color)

    def makeSound(self):
        print("Default sound")

class Fish(Animal):
    def __init__(self, name, age, color=None) -> None:
        super().__init__(name, age, False, True, color)

    def makeSound(self):
        pass

class Woodpecker(Bird):
    def __init__(self, name, age,) -> None:
        super().__init__(name, age, "Black and Red")

    def makeSound(self):
        print("Puk Puk")

class Parrot(Bird):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age, color)

    def makeSound(self):
        print("Im saying random word")

class Tiger(LandAnimal):
    def __init__(self, name, age, color=None) -> None:
        super().__init__(name, age, True, color)

    def makeSound(self):
        print("Roarrr!")

class Cow(LandAnimal):
    def __init__(self, name, age, color=None) -> None:
        super().__init__(name, age, False, color="Black and White")

    def makeSound(self):
        print("Muuuuuuu!")

class Shark(Fish):
    def __init__(self, name, age, color=None) -> None:
        super().__init__(name, age, False, True, color)

    def makeSound(self):
        print("Brrrr")

class Carp(Fish):
    def __init__(self, name, age, color=None) -> None:
        super().__init__(name, age, color)

    def makeSound(self):
        print("Bul bul!")


carp = Carp("Zibi", 5, "Blue")
tiger = Tiger("Robert", 10, "Orange")
cow = Cow("Marlena", 4)
fish = Fish("Nemo", 2, "Orange and White")

print(issubclass(Carp, (Fish, Animal)))

print(tiger.isSwimmer())
print(cow.isSwimmer())

cow.makeSound()
tiger.makeSound()
fish.makeSound()
