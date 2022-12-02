import pytest

from phonebook import Phonebook

@pytest.fixture
def phonebook(tmpdir):
    return Phonebook(tmpdir)
    # yield phonebook
    # phonebook.clear()

def test_check_by_name(phonebook):
    phonebook.add("Jarri", "1234567890")
    assert "1234567890" == phonebook.lookup("Jarri")

def test_phonebook_have_all_names(phonebook):
    phonebook.add("Jarri", "1234567890")
    assert "Jarri" in phonebook.names()


def test_missing_name_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Jarri")

