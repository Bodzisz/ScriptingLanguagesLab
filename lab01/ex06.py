first_names = []
second_names = []
names = []


def takeChoiceInput():
    return input("Your choice: ")


def processNewEmployee():
    print()
    first_name = input("First name: ")
    second_name = input("Second name: ")
    first_names.append(first_name)
    second_names.append(second_name)
    names.append(first_name + " " + second_name)
    print()
    print('Hello {fn:s} {sn:s}'.format(fn=first_name, sn=second_name))
    print("Your email is ", first_name.lower() + '.' + second_name.lower()
          + "@pwr.edu.pl")
    print()


def printOptions():
    print("1. Add new employee")
    print("2. exit")


exit = False
while not exit:
    printOptions()
    choice = takeChoiceInput()
    if choice == '1':
        processNewEmployee()
    else:
        exit = True
