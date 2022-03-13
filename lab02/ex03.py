import random


def rollDice():
    return random.randint(1, 6)


def rollRound():
    sum = 0
    for i in range(4):
        roll = rollDice()
        print(roll)
        sum += roll
    print()
    return sum


firstRound = rollRound()
secondRound = rollRound()
print("First round:", firstRound)
print("Second round:", secondRound)
if firstRound > secondRound:
    print("First round was higher")
elif firstRound < secondRound:
    print("Second round was higher")
else:
    print("Rounds were equal")
