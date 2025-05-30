# Here begins a new world...

from datetime import datetime

def get_days_from_today(date):
    
    """
    Обчислює кількість днів між поточною датою та заданою датою.

    Параметри:
    - date_str (str): дата у форматі 'YYYY-MM-DD'

    Повертає:
    - int: кількість днів між сьогоднішньою датою та заданою
    """

    today = datetime.now().date()
    my_date = string_to_date(date)

    days = (today - my_date).days

    return days

def input_date():

    """
    Запитує у користувача дату (рік, місяць, день), перевіряє її на валідність 
    та підтвердження. Повертає рядок дати у форматі 'YYYY-MM-DD'.

    Повертає:
    - str: коректно введена та підтверджена дата у форматі 'YYYY-MM-DD'
    """

    while True:
        print("Введіть свою дату")
        try:
            # Перевіряємо правильність введення року
            while True:
                y = int(input("Введіть рік (у форматі РРРР): "))
                if y > 0:
                    break
                else:
                    print("Рік не можу бути від'ємним. Введіть правильне значення")
                    continue
            
            # Перевіряємо правильність введення місяця
            while True:
                m = int(input("Введіть місяць (у форматі ММ): "))
                if 1 <= m <= 12:
                    break
                else:
                    print("Такого місяця не існує, їх усього 12. Тому введи правильне значення.")
                    continue
            
            # Перевіряємо правильність введення дня
            while True:
                d = int(input("Введіть день (у форматі ДД): "))
                if 1 <= d <= 31:
                    break
                else:
                    print("В місяці максимум 31 день, тому введіть правильне число.")
                    continue

        except ValueError:
            print("Ви ввели неправильне значення. Введіть цифрові значення")
            continue

        print(f"Ви ввели: {y:04d}-{m:02d}-{d:02d} !\nЦе правильно?\n(1 - Так; 2 - Ні)")
        
        # Перевірка та підтвердження введення правильності дати
        while True:
            try:
                choice = int(input())
                if choice == 1:
                    date = str(f"{y:04d}-{m:02d}-{d:02d}")
                    return date
                elif choice == 2:
                    print("Повернення на початок.")
                    break
                else:
                    print("Ви ввели невірне значення.\nПотрібно ввести: 1 - Так; 2 - Ні")
                    continue
            except ValueError:
                print("Ви ввели невірне значення, має бути число.")
        

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

# Запуск програми
print(get_days_from_today(input_date()))





