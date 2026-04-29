import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def test_mask_account_card_valid():
    """Функция тестирует стандартный номер карты"""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize("data, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                            ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                                            ("Счет 73654108430135874305", "Счет **4305"),
                                            ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
                                            ("МИР 2222333344445555", "МИР 2222 33** **** 5555"),
                                            ("Счет 12345678901234567890", "Счет **7890")])
def test_mask_account_card_valid(data, expected):
    """Функция, которая тестирует правильность ввода и вывода номера карты или счета"""
    assert mask_account_card(data) == expected


@pytest.fixture
def test_get_date_valid():
    """Функция тестирует правильность преобразования даты"""
    assert get_date("2024-03-11Т02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("data, expected", [("2024-03-11Т02:26:18.671407", "11.03.2024"),
                                            ("2025-08-17Т03:15:21.763109", "17.08.2025"),
                                            ("2025/08/17Т03:15:21.763109", "17.08.2025"),
                                            ("2025.08.17Т03:15:21.763109", "17.08.2025")])
def test_get_date_valid(data, expected):
    """Функция, которая тестирует корректный ввод и вывод даты"""
    assert get_date(data) == expected


def test_get_date_empty():
    """Функция, которая тестирует на наличие ошибок при отсутствии даты"""
    assert get_date("") is None
