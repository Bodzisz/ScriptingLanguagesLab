class Employee:
    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName
        self.fullName = firstName + " " + secondName
        self.email = firstName.lower() + '.' + secondName.lower() + "@pwr.edu.pl"

    def __str__(self):
        return '{n:20s} {sn:20s} {fn:20s} {e:20s}'.format(n=self.firstName, sn=self.secondName, 
        fn=self.fullName, e=self.email)


employees = []


def takeChoiceInput():
    return input("Your choice: ")


def processNewEmployee():
    print()
    first_name = input("First name: ")
    second_name = input("Second name: ")
    employees.append(Employee(first_name, second_name))
    print('Hello {fn:s} {sn:s}'.format(fn=first_name, sn=second_name))
    print("Your email is ", first_name.lower() + '.' + second_name.lower()
          + "@pwr.edu.pl")
    print()


def printOptions():
    print("1. Add new employee")
    print("2. Print employees")
    print("3. Exit")


exit = False
while not exit:
    printOptions()
    choice = takeChoiceInput()
    if choice == '1':
        processNewEmployee()
    elif choice == '2':
        for employee in employees:
            print(employee)
    else:
        exit = True