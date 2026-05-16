import allure
import requests
import pytest
from data import *
from helpers import *

class TestCreateOrder:
    @allure.title("Проверка создания заказа  авторизованным пользователем")
    def test_create_order_with_authorization(self, create_and_delete_user):
        token = create_and_delete_user[2]
        with allure.step("Отправка POST‑запроса на создание заказа с авторизацией"):
            response = requests.post(
                Endpoints.create_order,
                headers={'Authorization': token},
                data=Ingredients.burger
            )

        with allure.step("Проверка успешного ответа (success=True)"):
            assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Проверка создания заказа  неавторизованным пользователем")
    def test_create_order_without__authorization(self, create_and_delete_user):
        with allure.step("Отправка POST‑запроса на создание заказа без авторизации"):
            response = requests.post(
                Endpoints.create_order,
                data=Ingredients.burger
            )

        with allure.step("Проверка успешного ответа (success=True) для неавторизованного пользователя"):
            assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Проверка создания заказа  авторизованным пользователем без ингредиентов")
    def test_create_order_with_authorization_no_ingredients(self, create_and_delete_user):
        token = create_and_delete_user[2]
        with allure.step("Отправка POST‑запроса на создание заказа без ингредиентов (с авторизацией)"):
            response = requests.post(
                Endpoints.create_order,
                headers={'Authorization': token},
                data=Ingredients.burger_empty
            )

        with allure.step("Проверка кода ответа 400"):
            assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Проверка создания заказа  авторизованным пользователем с неправильным хемем ингридиентов")
    def test_create_order_with_authorization_wrong_hash(self, create_and_delete_user):
        token = create_and_delete_user[2]
        with allure.step("Отправка POST‑запроса на создание заказа с неправильным хешем ингредиентов (с авторизацией)"):
            response = requests.post(
                Endpoints.create_order,
                headers={'Authorization': token},
                data=Ingredients.burger_wrong_hash
            )

        with allure.step("Проверка кода ответа 500"):
            assert response.status_code == 500 and 'Internal Server Error' in response.text