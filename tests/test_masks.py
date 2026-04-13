import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """ Функция, которая тестирует правильность ввода и вывода номера карты """
    assert get_mask_card_number("5555222233337777") == "5555 22** **** 7777"


def test_get_mask_account():
    """ Функция, которая тестирует правильность ввода и вывода номера счета """
    assert get_mask_account("73654108430135874305") == "**4305"
