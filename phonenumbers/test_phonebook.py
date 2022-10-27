import unittest

from phonebook import Phonebook


class PhoneBookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = Phonebook()

    def test_lookup_by_name(self):

        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")

        self.assertEqual("12345", number)

    def test_missing_name(self):

        with self.assertRaises(KeyError):
            self.phonebook.lookup("Alex")

    def test_empty_phonebook_is_consistent(self):

        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_deuplicate_number(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")  # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")  # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())
