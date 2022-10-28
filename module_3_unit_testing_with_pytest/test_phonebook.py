import pytest

from module_3_unit_testing_with_pytest.phonebook import Phonebook


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Alex", "12345")

    assert "12345" == phonebook.lookup("Alex")


def test_phonebook_contains_all_names():
    phonebook = Phonebook()
    phonebook.add("Alex", "12345")

    assert "Alex" in phonebook.names()


def test_missing_name_raises_error():
    phonebook = Phonebook()
    phonebook.add("Alex", "12345")

    with pytest.raises(KeyError) as error:
        phonebook.lookup("John")

    assert error.type == KeyError
