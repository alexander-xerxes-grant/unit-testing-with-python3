from module_3_unit_testing_with_pytest.phonebook import Phonebook


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Alex", "12345")

    assert "12345" == phonebook.lookup("Alex")
