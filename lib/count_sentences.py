class MyString:
    def __init__(self, value=""):
        self.value = value  # This will call the setter below

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = val

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]', self.value)
        return len([s for s in sentences if s.strip()])
