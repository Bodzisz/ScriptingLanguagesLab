class Controlled_text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self._text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, input_text):
        for character in input_text:
            if str.isspace(character):
                raise Exception("Given text has spaces!")
        if not str.isprintable(input_text):
            raise Exception("Given text is not printable!")
        elif len(input_text) < 1:
            raise Exception("Given text's length is lower than 1!")
        else:
            self._text = input_text

    def __gt__(self, other):
        if self.text > other.text:
            return True
        return False

    def __lt__(self, other):
        if self.text < other.text:
            return False
        else:
            return True

    def __eq__(self, other):
        if self.text == other.text:
            return True
        else:
            return False

blabla = Controlled_text("lala")