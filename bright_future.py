# Импортируйте необходимые модули.
from datetime import datetime


def validate_record(name: str, birthdate: str) -> bool:
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(birthdate, '%d.%m.%Y')
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birthdate}')
        return False


def process_people(entries: list[tuple]) -> dict:
    # Объявите счётчики.
    bad_count = 0
    good_count = 0
    statistics = {}
    for i in entries:
        if validate_record(i[0], i[1]):
            good_count += 1
        else:
            bad_count += 1

    statistics['good'] = good_count
    statistics['bad'] = bad_count
    # Распакуйте кортежи из полученного списка entries.
    # Каждую пару значений передайте в validate_record(),
    # чтобы проверить корректность формата даты рождения.
    # В зависимости от результата проверки увеличьте один из счётчиков.

    # Верните словарь.
    return statistics


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')
