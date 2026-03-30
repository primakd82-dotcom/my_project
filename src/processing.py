""" Функция, которая принимает список словарей и
опционально значение для ключа state (по умолчанию "EXECUTED").
Функция возвращает новый список словарей, содержащий только те словари,
у которых ключ state соответствует указанному значению.

Пример ввода:
[
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]"""


def filter_by_state(data_list, status='EXECUTED') -> list:
    """ Функция возвращает новый список словарей, содержащий только те словари,
     у которых ключ state соответствует указанному значению. """
    new_list = []

    for item in data_list:
        if item.get('state') == status:
            new_list.append(item)

    return new_list


data_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print(filter_by_state(data_list))


def sort_by_date(data_list, descending=True) -> list:
    """ Функция возвращает новый список,
    отсортированный по дате (date) на убывание """
    return sorted(data_list, key=lambda x: x.get('date'), reverse=descending)


print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]))
