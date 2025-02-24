from typing import Optional


class User:
    def __init__(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            username: str | None = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(cls, first_name: str, last_name: str):
        return cls(first_name=first_name, last_name=last_name)

    # Опишите метод класса with_username.
    @classmethod
    def with_username(cls, username: str):
        cls.is_username_allowed(username)
        return cls(username='@'+username)

        # Опишите статический метод класса is_username_allowed.

    @staticmethod
    def is_username_allowed(username: str):
        if username.startswith('admin'):
            print('Некорректное имя пользователя')
            return False
        return True

    # Опишите метод-свойство full_name.
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
# ne_stas = User.with_username('admin_blabla')
