class Employee:
    vacation_days = 28

    # инициализируем
    def __init__(self, first_name, second_name, gender):

        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, consume_vacations):

        self.remaining_vacation_days -= consume_vacations
        return self.remaining_vacation_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    def result(self):

        return (f'Имя: {self.first_name}, Фамилия: {self.second_name},'
                f'Пол: {self.gender}, Отпускных дней в году:'
                f'{Employee.vacation_days}.')


class FullTimeEmployee(Employee):

    def get_unpaid_vacation(self, start_date, duration):
        return (f'Начало неоплачиваемого отпуска: {start_date},'
                f' продолжительность: {duration} дней.')


class PartTimeEmployee(Employee):

    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days

    def get_unpaid_vacation(self, start_date, duration):

        return (f'Начало неоплачиваемого отпуска: {start_date},'
                f'продолжительность: {duration} дней.')


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name='Роберт',
                     second_name='Крузо', gender='м')
employee2 = Employee(first_name='Анна', second_name='Смит', gender='ж')
used_days_emp1 = 7
used_days_emp2 = 13

# Допишите код для вывода информации о сотрудниках.
# print(employee1.result())
# employee1.consume_vacation(used_days_emp1)
# print(employee1.get_vacation_details())
# print(employee2.result())
# employee2.consume_vacation(used_days_emp2)
# print(employee2.get_vacation_details())

# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())
