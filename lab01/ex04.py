from re import T


def is_primary(number):
    if number <= 2:
        return False
    if number == 3:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
        i = i * i - 1
    return True

def getDividers(number):
    dividers = []
    for i in range(2, number):
        if number % i == 0:
            dividers.append(i)
    return dividers

def firstDot(list):
    for number in list:
        if is_primary(number):
            print(number, " is primary number")
        else:
            print(number, " has dividers: ", getDividers(number))

def secondDot(list):
    print(sorted(list))
    print(sorted(list, reverse=True))

def thirdDot(list):
    print("Before: ", list)
    print("After: ", sorted(list[0:3]) + list[3:])


list = [ 19, 3, 15, 43, 98, 16, 9, 23, 4]
firstDot(list)
print('\n')

secondDot(list)
print("\n")

thirdDot(list)




