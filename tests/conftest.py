import allure
import pytest
import random
import string

from handlers.handlers import post_create_courier


@allure.step(f'Генерация даннях для создания курьера')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


@pytest.fixture(scope="function")
@allure.step(f'Подготавливаем словарь с данными для создания курьера')
def generate_and_return_login_password():
    login_pass = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }
    return login_pass


@pytest.fixture(scope="function")
@allure.step(f'Регистрация курьера')
def register_new_courier_and_return_login_password():
    body = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

    response = post_create_courier(body=body)

    if response.status_code == 201:
         return body
