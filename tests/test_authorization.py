import allure
import requests
import pytest
from data import *
from helpers import *

class TestAuthorization:
    @allure.title("Проверка авторизации пользователя")
    def test_authorization_user(self, create_and_delete_user):
        payload = create_and_delete_user[1]
        login = payload.copy()
        login.pop("name")
        with allure.step("Отправка POST‑запроса на авторизацию пользователя"):
            response = requests.post(Endpoints.login_user, data=login)
        with allure.step("Проверка успешного ответа (success=True)"):
            assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Проверка авторизации пользователя c неправильным логином и паролем код ответа")
    def test_authorization_user_code(self):
        payload = UserData.bad_login
        with allure.step("Отправка POST‑запроса с некорректными данными"):
            response = requests.post(Endpoints.login_user, data=payload)
        with allure.step("Проверка кода ответа 401"):
            assert response.status_code == 401

    @allure.title("Проверка авторизации пользователя c неправильным логином и паролем текст ответа")
    def test_authorization_user_message(self):
        payload = UserData.bad_login
        with allure.step("Отправка POST‑запроса с некорректными данными"):
            response = requests.post(Endpoints.login_user, data=payload)

        with allure.step("Проверка сообщения об ошибке в ответе"):
            assert response.json()['message'] == "email or password are incorrect"

