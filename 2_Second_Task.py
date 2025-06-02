# Here begins a new world...

import random

def get_numbers_ticket(min, max, quantity):

    """
    Генерує відсортований список унікальних випадкових чисел.

    Аргументи:
    - min (int): найменше можливе число (діапазон початку)
    - max (int): найбільше можливе число (діапазон кінця)
    - quantity (int): скільки чисел потрібно обрати

    Повертає:
    - list[int]: Відсортований список унікальних чисел, якщо параметри валідні
    - list[]: Порожній список, якщо параметри не відповідають вимогам
    """

    # Перевірка валідності введених даних
    if min < 1 or max > 1000:
        print("Межі діапазону мають бути в межах від 1 до 1000.")
        return []
    
    if quantity < min or quantity > max:
        print(f"Кількість чисел має бути в діапазоні від {min} до {max}.")
        return []
    
    # Створюємо робочий список чисел
    work_space = list(range(min, max +1))

    # Обираємо випадкові унікальні числа без повторів
    new_list = random.sample(work_space, quantity)

    return sorted(new_list)

# Викликаємо функцію
numbers = get_numbers_ticket(1, 49, 8)
print("Ваші лотерейні номери:", numbers)
