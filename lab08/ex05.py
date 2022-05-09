import ex02, ex03, ex04, re

class Person:

    def __init__(self, first_name, last_name, id_num):
        self.first_name = ex02.First_name(first_name)
        self.last_name = ex03.Last_name(last_name)
        self.id = ex04.Ident_number(id_num)

    @staticmethod
    def fromString(value):
        fields = re.split(' |;|/', value)
        if len(fields) != 3:
            raise Exception("Wrong number of arguments!")
        return Person(fields[0].strip(), fields[1].strip(), fields[2].strip())

    def __str__(self):
        return self.first_name.name + " " + self.last_name.lname + " " + self.id.num


# person = Person("jan", "Kowalski", "123456728")
# print(person)
