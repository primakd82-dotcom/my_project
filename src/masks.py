from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера"""
    card_number = str(card_number)
    mask = "** ****" + " "
    part_1 = card_number[:4] + " "
    part_2 = card_number[4:6]
    part_3 = card_number[12:16]
    return part_1 + part_2 + mask + part_3


card_number = 5555222233337777
print(get_mask_card_number(card_number))


def get_mask_account(user_account: Union[int, str]) -> str:
    """Функция маскировки банковского счета"""
    user_account = str(user_account)
    mask = "**"
    part = user_account[-4:]
    return mask + part


user_account = 73654108430135874305
print(get_mask_account(user_account))
