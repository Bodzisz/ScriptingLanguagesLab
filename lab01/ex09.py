users = {1234: 1500, 4321: 15000, 2137: 123000}


def logIn():
    try:
        return int(input("Enter PIN: "))
    except ValueError as e:
        print('You need to enter an integer number.', e)
        return logIn()


def takeChoiceInput():
    return input("Your choice: ")


def printMenu():
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Log out")


def getBalance(pin):
    return users[pin]


def withdrawCash(pin):
    amount = int(input("\nEnter amount to withdraw: "))
    if users[pin] > 0 and users[pin] >= amount:
        print(amount, " is withdrawn!\n")
        users[pin] = users[pin] - amount
    else:
        print("\nNot enough founds!\n")


input_pin = logIn()
if input_pin in users.keys():
    exit = False
    while not exit:
        printMenu()
        choice = takeChoiceInput()
        if choice == '1':
            print("\nYour balance: ", getBalance(input_pin), "\n")
        elif choice == '2':
            withdrawCash(input_pin)
        else:
            print("\n Logged out!\n")
            exit = True
else:
    print("Wrong PIN!")
