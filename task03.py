import re
from typing import List

def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone number to the international format.

    Parameters:
    phone_number (str): The raw phone number string.

    Returns:
    str: The normalized phone number in international format or 'Invalid phone number'.
    """
    pattern = r"\D"
    replacement = ""
    
    phone_number = re.sub(pattern, replacement, phone_number)

    if len(phone_number) == 12:
        return f'+{phone_number}'
    elif len(phone_number) == 11:
        return f'+3{phone_number}'
    elif len(phone_number) == 10:
        return f'+38{phone_number}'
    else:
        return 'Invalid phone number'

# Example usage
raw_numbers: List[str] = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050)123-32-34",
    " 0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
    " 8(950)1234567",
    " 1234567",
    "123-456",
    "38050123ABCD",
    "\\380501234567"
    
]

sanitized_numbers: List[str] = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)