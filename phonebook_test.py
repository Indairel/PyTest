import pytest

class Phonebook:

    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())

def test_check_by_name():
    phonebook = Phonebook()
    phonebook.add("Jarri", "1234567890")
    assert "1234567890" == phonebook.lookup("Jarri")

def test_phonebook_have_all_names():
    phonebook = Phonebook()
    phonebook.add("Jarri", "1234567890")
    assert "Jarri" in phonebook.names()

def test_missing_name_error():
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("Jarri")

