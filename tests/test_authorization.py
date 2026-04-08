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
        response = requests.post(Endpoints.login_user, data=login)
        assert response.json()["success"] is True

    @allure.title("Проверка авторизации пользователя c неправильным логином и паролем код ответа")
    def test_authorization_user_code(self):
        payload = UserData.bad_login
        response = requests.post(Endpoints.login_user, data=payload)
        assert response.status_code == 401 

    @allure.title("Проверка авторизации пользователя c неправильным логином и паролем текст ответа")
    def test_authorization_user_message(self):
        payload = UserData.bad_login
        response = requests.post(Endpoints.login_user, data=payload)
        assert response.json()['message'] == "email or password are incorrect"    


