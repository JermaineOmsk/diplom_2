import allure
import requests
import pytest
from data import *
from helpers import *

class TestCreateCourier:
    @allure.title("Проверка  регистрации нового пользователя")
    def test_create_user(self, create_and_delete_user):
        response = create_and_delete_user[0]
        assert response.json()["success"] is True


    @allure.title("Проверка  регистрации уже имеющегося пользователя текст ответа")
    def test_create_duplicate_user_message(self, create_and_delete_user):
        payload = create_and_delete_user[1]
        response = requests.post(Endpoints.create_user, data=payload)
        assert response.json()["message"] == "User already exists"

    @allure.title("Проверка  регистрации уже имеющегося пользователя код ответа")
    def test_create_duplicate_user_code(self, create_and_delete_user):
        payload = create_and_delete_user[1]
        response = requests.post(Endpoints.create_user, data=payload)
        assert response.status_code == 403


    @allure.title("Проверка  регистрации  пользователя c пустым полем текст ответа")
    @pytest.mark.parametrize('payload', (UserData.no_email, UserData.no_name, UserData.no_password))
    def test_create_user_withot_email_message(self,payload):
        response = requests.post(Endpoints.create_user, data=payload)
        assert response.json()["message"] == "Email, password and name are required fields"    

    @allure.title("Проверка  регистрации  пользователя c пустым полем  код ответа")
    @pytest.mark.parametrize('payload', (UserData.no_email, UserData.no_name, UserData.no_password))
    def test_create_user_withot_email_code(self, payload):
        response = requests.post(Endpoints.create_user, data=payload)
        assert response.status_code == 403