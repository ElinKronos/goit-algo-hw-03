# Here begins a new world...

import re

def normalize_phone(phone_number):
    
    """
    Функція приймає рядок з номером телефону у довільному форматі
    та повертає його у стандартизованому вигляді для SMS-розсилки:
    лише цифри + міжнародний код +380 (для України).
    
    Аргументи:
    phone_number (str): Номер телефону у довільному форматі.

    Повертає:
    str: Нормалізований номер телефону.
    """

    # Видаляємо всі символи, які не є цифрами
    clean_number = re.sub(r"\D", "", phone_number)

    # Перевіряємо початок номеру телефону та додаємо невистачаючі символи
    if clean_number.startswith("380"):
        return '+' + clean_number
    
    elif clean_number.startswith("+380"):
        return clean_number
    
    elif clean_number.startswith("0"):
        return '+38' + clean_number

# Чорновий список наших номерів
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Застосовуємо нормалізацію до кожного номеру
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Виводимо готовий результат
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)