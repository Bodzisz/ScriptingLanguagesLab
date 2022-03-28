import string


class Student:
    university = "PWR"

    def __init__(self, name, index, age):
        self.setName(name)
        self.index = index
        self.setAge(age)

    def age(self):
        return self.age

    def print(self):
        print('{n:20s} {index:20s} {a: 2d}'.format(n=self.name, index=self.index, a=self.age))

    @setPrinter
    def setName(self, name):
        if isinstance(name, string):
            self.name = name
        else:
            raise TypeError("Name must be string type")

    def setPrinter(self):
        print("Setting value ...")

    @setPrinter
    def setIndex(self, index):
        self.index = index

    @setPrinter
    def setAge(self, age):
        if isinstance(age, int):
            if age > 0:
                self.age = age
            else:
                raise ValueError("Age must be positive number")
        else:
            raise TypeError("Age must be integer type")

    def delPrice(self):
        del price

    age = property(fget=age, fset=setAge, fdel= delPrice, doc = 'Student age.')


student1 = Student("Kacper", "260388", 20)
student2 = Student("Mariusz", "260389", 22)
student3 = Student("Robert", "260390", 21)
student4 = Student("Jan", "260391", 19)

students = []
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)

for student in students:
    student.print()

student1.year = 2
student2.laptop = "hp"
student3.fromWroclaw = True
student4.secondName = "Michal"
print(student1.year)
print(student2.laptop)
print(student3.fromWroclaw)
print(student4.secondName)
