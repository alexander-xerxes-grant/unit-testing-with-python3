from zlib import DEF_BUF_SIZE


class Phonebook:
    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())
