import ex01

class Ident_number(ex01.Controlled_text):

    def __init__(self, num):
        super().__init__(num)
        self.num = num

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        if str.isnumeric(value) and len(value) == 9:
            lastTwoDigits = int(value[len(value)-2:])
            firstSevenDigits = 0

            for number in value[:7]:
                firstSevenDigits += int(number)
            if firstSevenDigits == lastTwoDigits % 97:
                self._num = value
            else:
                raise Exception("Wrong control number!")
        else:
            raise Exception("Number must be 9 digits!")

    def __str__(self):
        return self.num


# id = Ident_number("123456728")
# print(id)

