import random


def createNumbers():
    numbers = set([])
    while len(numbers) != 6:
        numbers.add(random.randint(0, 49))
    return numbers


def takeGuesses():
    guesses = []
    for i in range(6):
        guesses.append(int(input("Your guess: ")))
    return guesses


def getRightGuesses(numbers, guesses):
    counter = 0
    for guess in guesses:
        if guess in numbers:
            counter += 1
    return counter


numbers = createNumbers()
guesses = takeGuesses()
print("Correct guesses: ", getRightGuesses(numbers, guesses))
print("Actual numbers: ", numbers)
