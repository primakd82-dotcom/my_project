def filter_by_currency(transactions, currency):
    """ Функция, которая возвращает итератор по транзакциям с заданной валютой. """
    filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    return filtered_transactions

