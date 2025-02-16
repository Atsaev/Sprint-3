class MushroomsCollector:
    # Проверьте, нет ли здесь ошибки:
    def __init__(self):
        self.mushrooms = []

    # Исправьте ошибку в этом методе.
    def is_poisonous(self, mushroom_name: str) -> bool:
        if mushroom_name == 'Мухомор' or mushroom_name == 'Поганка':
            return True
        return False

    # Допишите метод.
    def add_mushroom(self, mushroom_name: str) -> None:
        if self.is_poisonous(mushroom_name):
            print('Нельзя добавить ядовитый гриб')
        else:
            self.mushrooms.append(mushroom_name)  # Добавьте гриб в список

    # Напишите магический метод __str__,
    # возвращающий перечень грибов из списка mushrooms
    # через запятую.
    def __str__(self):
        # Верните строку с грибами через запятую
        return ', '.join(self.mushrooms)


# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)
