users = {}


def printMenu():
    print("1. Create Account")
    print("2. Log In")
    print("3. Print Users")
    print("4. Quit")


def takeChoiceInput():
    return input("Your choice: ")


def createAccount():
    print()
    nick = input("Nick: ")
    first_name = input("First Name: ")
    second_name = input("Second Name: ")
    input("Email: ")
    email = first_name.lower() + '.' + second_name.lower() + "@pwr.edu.pl"
    print("Account created with nickname: ", nick)
    print("We have to create email with @pwr.edu.pl domain")
    print("Your email is ", email)
    print()
    users[nick] = (first_name, second_name, email)


def printUsers():
    print()
    for user in users:
        print(user, ": ", users[user])
    print()


def logIn():
    print()
    input_email = input("Enter your nick: ")
    if input_email in users.keys():
        print("Log in is successfull")
    else:
        print("Log in is not possible")
    print()


exit = False
while not exit:
    printMenu()
    choice = takeChoiceInput()
    if choice == '1':
        createAccount()
    elif choice == '2':
        logIn()
    elif choice == '3':
        printUsers()
    else:
        exit = True
