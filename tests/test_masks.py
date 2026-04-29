import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def get_mask_card_number_valid():
    """ Функция тестирует стандартный 16 значный номер карты """
    assert get_mask_card_number("5555222233337777") == "5555 22** **** 7777"


@pytest.mark.parametrize("card_number, expected", [("5555222233337777", "5555 22** **** 7777")])
def test_get_mask_card_number_valid(card_number, expected):
    """ Функция, которая тестирует правильность ввода и вывода номера карты """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_number", [("555522223333", "fanfekgrldofgrgd",
                                             "", None)])
def test_get_mask_card_number_invalid(invalid_number):
    """ Функция, которая тестирует некорректные данные """
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_number)


@pytest.mark.parametrize("user_account, expected", [("73654108430135874305", "**4305")])
def test_get_mask_account(user_account, expected):
    """ Функция, которая тестирует правильность ввода и вывода номера счета """
    assert get_mask_account(user_account) == expected
