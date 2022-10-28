from unicodedata import name

from Module 3 Unit Testing with pytest.phonebook import Phonebook


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Alex", "12345")

    assert "12345" == phonebook.lookup("Alex")