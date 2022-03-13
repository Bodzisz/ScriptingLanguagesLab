import random

suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
figures = ["Ace", "King", "Queen", "Jack", "Ten", "Nine"]


def getFullDeck():
    return [(x, y) for x in figures for y in suits]


def shuffleCards(cards):
    random.shuffle(cards)


def dealCards(cards, n):
    dealedCards = []
    for i in range(n):
        if(len(cards) != 0):
            dealedCards.append(cards[0])
            cards.pop(0)
    return dealedCards


def game(player1: list, player2: list):
    exit = False
    while not exit:
        shuffleCards(player1)
        shuffleCards(player2)
        player1Card = player1.pop(0)
        player2Card = player2.pop(0)
        print("Player1: ", player1Card, " VS Player2: ", player2Card)
        if powerOfCards[player1Card[0]] == powerOfCards[player2Card[0]]:
            print("BATTLE DROWN!")
            player1.append(player1Card)
            player2.append(player2Card)
        elif powerOfCards[player1Card[0]] > powerOfCards[player2Card[0]]:
            print("PLAYER1 WINS BATTLE!")
            player1.append(player1Card)
            player1.append(player2Card)
        else:
            print("PLAYER2 WINS BATTLE!")
            player2.append(player2Card)
            player2.append(player1Card)

        if len(player1) == 0:
            print("PLAYER 2 WON THE WAR!")
            exit = True
        elif len(player2) == 0:
            print("PLAYER 1 WON THE WAR!")
            exit = True
        else:
            print("RESULT: ", len(player1), " VS ", len(player2))


cards = getFullDeck()
shuffleCards(cards)

player1 = dealCards(cards, 5)
player2 = dealCards(cards, 5)
print(player1)
print(player2)

powerOfCards = {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11, "Ten": 10,
                "Nine": 9}
# player1.sort(key=lambda x: powerOfCards[x[0]])
# player2.sort(key=lambda x: powerOfCards[x[0]])
shuffleCards(player1)
shuffleCards(player2)
game(player1, player2)
