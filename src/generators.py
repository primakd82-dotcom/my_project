def filter_by_currency(transactions, currency):
    """ Функция, которая возвращает итератор по транзакциям с заданной валютой. """
    filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    return filtered_transactions


def transaction_descriptions(transactions):
    """ Генератор, который принимает список словарей с транзакциями и возвращает
        описание каждой операции по очереди. """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """ Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX. """
    for number in range(start, stop+1):
        numbers = str(number).zfill(16)
        format_num = f"{numbers[:4]} {numbers[4:8]} {numbers[8:12]} {numbers[12:]}"
        yield format_num
        if numbers == "9999999999999999":
            break
