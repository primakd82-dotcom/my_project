def mask_account_card(data: str) -> str:
    """Функция, которая принимает тип и номер карты или счета
    и возвращает строку с замаскированным номером"""
    parts = data.split()
    account_type = " ".join(parts[:-1])
    number = parts[-1]

    if "счет" in data.lower() or "Счет" in data:
        masked_number = "**" + number[-4:]
    else:
        clean_number = number.replace(" ", "")
        if len(clean_number) == 16:
            masked_number = f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"
        else:
            masked_number = "**** " + clean_number[-4:]

    return f"{account_type} {masked_number}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))