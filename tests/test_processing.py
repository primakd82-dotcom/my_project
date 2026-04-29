import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def status_items():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


def test_filter_by_state_executed(status_items):
    """ Функция, которая тестирует фильтрацию по заданному статусу """
    result = filter_by_state(status_items, 'EXECUTED')
    assert result == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_by_state_canceled(status_items):
    """ Функция, которая тестирует фильтрацию по заданному статусу """
    result = filter_by_state(status_items, 'CANCELED')
    assert result == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


def test_filter_by_state_not_found(status_items):
    """ Функция, которая тестирует фильтрацию при отсутствии заданного статуса """
    result = filter_by_state(status_items, 'DELETE')
    assert result == []


@pytest.fixture
def date_items():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


def test_sort_by_date_descending(date_items):
    """ Функция, которая тестирует список,
        отсортированный по дате (date) на убывание """
    result = sort_by_date(date_items, descending=True)
    assert [item['id'] for item in result] == [41428829, 615064591, 594226727, 939719570]


def test_sort_by_date_ascending(date_items):
    """ Функция, которая тестирует список,
        отсортированный по дате (date) по возрастанию """
    result = sort_by_date(date_items, descending=False)
    assert [item['id'] for item in result] == [939719570, 594226727, 615064591, 41428829]


@pytest.mark.parametrize("transactions", [
    ([{'id': 41428829, 'date': '01-06-2023'}]),
    ([{'id': 939719570, 'date': '2023-15'}]),
    ([{'id': 594226727, 'date': ''}]),
    ([{'id': 615064591, 'date': None}]),
])
def test_sort_by_date_with_incorrect_formats(transactions):
    """ Функция, которая тестирует список
        с некорректными данными по статусу "date" """
    try:
        result = sort_by_date(transactions)
        assert isinstance(result, list)
    except Exception:
        pytest.fail('sort_by_date выбросила ошибку на некорректных датах')
