# Here begins a new world...

from datetime import datetime

def get_days_from_today(date):
    
    """
    Обчислює кількість днів між поточною датою та заданою датою.

    Параметри:
    - date (str): дата у форматі 'YYYY-MM-DD'

    Повертає:
    - int: кількість днів між сьогоднішньою датою та заданою
    """

    today = datetime.now().date()
    
    try:
        date_parts = date.strip().split("-")
                
        if len(date_parts) != 3:
            print("Ви ввели невірний формат дати.")
            return 
        
        year, month, day = date_parts

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            print("Ви ввели невірне значення дати.")
            return 

        if not (int(year) > 0 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            print("Ви ввели невірний діапазон дати.")
            return 
    
        my_date = string_to_date(date)
        days = (today - my_date).days
        return days
        
    except ValueError:
        print("Введено некоректні дані")

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

# Запуск програми
print(get_days_from_today("2011-11-12"))





