import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


@pytest.mark.parametrize("currency, expected_ids", [("USD", [939719570, 142264268, 895315941]),
                                                    ("RUB", [873106923, 594226727]),
                                                    ("EUR", [])])
def test_filter_by_currency(currency, expected_ids):
    """ Функция, которая тестирует корректность фильтрации транзакций по заданной валюте """
    result = list(filter_by_currency(transactions, currency))
    ids = [tx["id"] for tx in result]
    assert ids == expected_ids


@pytest.mark.parametrize("transactions, expected_descriptions", [
    ([
         {'description': 'Перевод организации'},
         {'description': 'Перевод со счета на счет'},
         {'description': 'Перевод со счета на счет'},
         {'description': 'Перевод с карты на карту'},
         {'description': 'Перевод организации'}
     ],
     [
         "Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
         "Перевод с карты на карту", "Перевод организации"
     ]),
    ([], [])
])
def test_transaction_descriptions(transactions, expected_descriptions):
    """ Функция, которая возвращает корректные описания для каждой транзакции """
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


@pytest.fixture
def card_number():
    return "0000000000000000"


def test_card_number_generators(card_number):
    """ Тестирование функции на корректность длины номера карт и состоят ли они из цифр """
    assert len(card_number) == 16
    assert card_number.isdigit()


def test_card_number_generator():
    gen = card_number_generator(1, 3)
    result = list(gen)
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]


def test_card_number_generator_min():
    gen = card_number_generator(0, 0)
    result = list(gen)
    assert result == ["0000 0000 0000 0000"]


def test_card_number_generator_max():
    gen = card_number_generator(9999999999999999, 9999999999999999)
    result = list(gen)
    assert result == ["9999 9999 9999 9999"]
