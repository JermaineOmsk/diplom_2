import allure
import string
import random
@allure.step('Генерация случайной строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Создание нового пользователя ')
def create_user():
    user_email = f'{generate_random_string(10)}@mail.ru'
    user_password = generate_random_string(10)
    user_name = generate_random_string(10)

    user = {
        "email": user_email,
        "password": user_password,
        "name": user_name
        }
    return user
        
