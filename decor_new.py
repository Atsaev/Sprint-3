# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        users_dict = func()
        obfuscated_name = users_dict['name']
        obfuscated_pass = users_dict['password']
        users_dict['name'] = obfuscated_name[0] + '*' * \
            (len(obfuscated_name) - 2) + obfuscated_name[-1]
        users_dict['password'] = '*' * len(obfuscated_pass)
        return users_dict
    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest',
    }


print(get_credentials())
