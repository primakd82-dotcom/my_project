import pytest
from src.masks import get_mask_card_number, get_mask_account, card_number


@pytest.fixture
def card_number():
    return [555522223333777]


def test_get_mask_card_number():
    """ Функция, которая тестирует правильность ввода и вывода номера карты """
    assert get_mask_card_number("5555222233337777") == "5555 22** **** 7777"


def test_get_mask_card_number_invalid_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number([555522223333777])


def test_get_mask_account():
    """ Функция, которая тестирует правильность ввода и вывода номера счета """
    assert get_mask_account("73654108430135874305") == "**4305"
