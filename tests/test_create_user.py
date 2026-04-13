import allure
import requests
import pytest
from data import *
from helpers import *

class TestCreateCourier:
    @allure.title("Проверка  регистрации нового пользователя")
    def test_create_user(self):
        with allure.step("Подготовка данных для регистрации нового пользователя"):
            payload = create_user()
        with allure.step("Отправка POST‑запроса на регистрацию нового пользователя"):
            response = requests.post(Endpoints.create_user, data=payload)    
        with allure.step("Проверка успешного создания нового пользователя (success=True)"):
            assert response.status_code == 200 and response.json()["success"] is True
        token = response.json()["accessToken"]
        with allure.step("Удаление созданного пользователя после теста"):
            requests.delete(Endpoints.data_user, headers={'Authorization': token})

    @allure.title("Проверка  регистрации уже имеющегося пользователя текст ответа")
    def test_create_duplicate_user_message(self, create_and_delete_user):
        payload = create_and_delete_user[1]
        with allure.step("Отправка POST‑запроса на регистрацию существующего пользователя"):
            response = requests.post(Endpoints.create_user, data=payload)


        with allure.step("Проверка сообщения об ошибке 'User already exists'"):
            assert  response.json()["message"] == "User already exists"

    @allure.title("Проверка  регистрации уже имеющегося пользователя код ответа")
    def test_create_duplicate_user_code(self, create_and_delete_user):
        payload = create_and_delete_user[1]
        with allure.step("Отправка POST‑запроса на регистрацию существующего пользователя"):
            response = requests.post(Endpoints.create_user, data=payload)

        with allure.step("Проверка кода ответа 403"):
            assert response.status_code == 403



    @allure.title("Проверка  регистрации  пользователя c пустым полем текст ответа")
    @pytest.mark.parametrize('payload', (UserData.no_email, UserData.no_name, UserData.no_password))
    def test_create_user_withot_email_message(self,payload):
        with allure.step("Отправка POST‑запроса на регистрацию с неполными данными"):
            response = requests.post(Endpoints.create_user, data=payload)

        with allure.step("Проверка сообщения об ошибке 'Email, password and name are required fields'"):
            assert  response.json()["message"] == "Email, password and name are required fields"
  

    @allure.title("Проверка  регистрации  пользователя c пустым полем  код ответа")
    @pytest.mark.parametrize('payload', (UserData.no_email, UserData.no_name, UserData.no_password))
    def test_create_user_withot_email_code(self, payload):
        with allure.step("Отправка POST‑запроса на регистрацию с неполными данными"):
            response = requests.post(Endpoints.create_user, data=payload)

        with allure.step("Проверка кода ответа 403"):
            assert response.status_code == 403