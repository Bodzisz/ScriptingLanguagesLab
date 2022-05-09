from zoneinfo import available_timezones
import ex01

class First_name(ex01.Controlled_text):
    availableNames = []

    def __init__(self, name):
        super().__init__(name)
        if len(self.availableNames) == 0:
            self.loadAvailableNames()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = value.capitalize()
        if value in First_name.availableNames:
            self._name = value
        else:
            raise Exception("Name not in file!")

    @classmethod
    def loadAvailableNames(cls):
        with open(r"C:\Users\kacpe\University\PD8Siem-1 (1)\PopularneImiona.txt", 'r', encoding="utf-8") as file:
                for line in file.readlines():
                    line = line.strip()
                    if line != "Kobiety" and line != "Mężczyźni":
                        cls.availableNames.append(line)

    @staticmethod
    def ismale(name):
        return not First_name.isfemale(name)

    @staticmethod
    def isfemale(name):
        if name[len(name) - 1] == 'a':
            return True
        return False

    def __str__(self):
        return self._name

# name = First_name("fiLiP")
# print(name)
# print(First_name.isfemale(name.name))
# print(First_name.ismale(name.name))
