class Employee:
    vacation_days = 28

    # инициализируем
    def __init__(self, first_name, second_name, gender):

        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

    def result(self):

        return (
            f'Имя: {self.first_name}, '
            f'Фамилия: {self.second_name}, Пол: {self.gender}, '
            f'Отпускных дней в году: {Employee.vacation_days}.'
        )


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name='Роберт', second_name='Крузо', gender='м')
employee2 = Employee(first_name='Анна', second_name='Смит', gender='ж')

# Допишите код для вывода информации о сотрудниках.
print(employee1.result())
print(employee2.result())
