from datetime import datetime, timedelta
from random import sample


def choose_days():
    first_month_half = list(range(1, 16))
    practice_days = sample(first_month_half, 3)  # Случайно выбираем 3 дня
    practice_days.sort()  # Сортируем выбранные дни
    now = datetime.now()

    for i in range(3):
        # Заменяем день в текущей дате на выбранный
        practice_date = now.replace(day=practice_days[i])
        print(f'{i + 1}-е занятие: {practice_date.strftime("%d.%m.%Y")}')


choose_days()
