import ex01

class Last_name(ex01.Controlled_text):

    def __init__(self, lname):
        super().__init__(lname)
        self.lname = lname

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, value):
        def check_single(last_name):
            if last_name[0].islower():
                raise Exception("Last names does not start with uppercase letters")
            elif not last_name[1:].islower():
                raise Exception("There are uppercase letters in last name!")

        if '-' in value:
            splited = value.split('-')
            if len(splited) != 2:
                raise Exception("Too many '-' in last name")
            check_single(splited[0])
            check_single(splited[1])
        check_single(value)
        self._lname = value

    def __str__(self):
        return self._lname


# last_name = Last_name("Nowak")
# print(last_name)


