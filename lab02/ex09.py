# *args
def sumNumbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(sumNumbers(1,2,3,4,5,6,7))

# *kwargs
def printTypes(**args):
    for key,value in args.items():
        print("{} : {} : {}".format(key, value, type(value)))

printTypes(Name = "Kacper", Age = 20, Points = 6.0, Male = True)

# funckja jako zmienna
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def calculate(operation, a, b):
    return operation(a,b)

addition = add
substraction = substract

print(calculate(addition, 1, 2))









