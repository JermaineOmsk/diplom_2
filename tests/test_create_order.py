import allure
import requests
import pytest
from data import *
from helpers import *

class TestCreateOrder:
    @allure.title("Проверка создания заказа  авторизованным пользователем")
    def test_create_order_with_authorization(self, create_and_delete_user):
        token = create_and_delete_user[2]
        response = requests.post(Endpoints.create_order,headers={'Authorization': token}, data=Ingredients.burger)
        assert response.json()["success"] is True

    @allure.title("Проверка создания заказа  неавторизованным пользователем")
    def test_create_order_without__authorization(self, create_and_delete_user):
        response = requests.post(Endpoints.create_order, data=Ingredients.burger)
        assert response.json()["success"] is  True

    @allure.title("Проверка создания заказа  авторизованным пользователем без ингредиентов")
    def test_create_order_with_authorization_no_ingredients(self, create_and_delete_user):
        token = create_and_delete_user[2]
        response = requests.post(Endpoints.create_order,headers={'Authorization': token}, data=Ingredients.burger_empty)
        assert response.status_code == 400  

    @allure.title("Проверка создания заказа  авторизованным пользователем с неправильным хемем ингридиентов")
    def test_create_order_with_authorization_wrong_hash(self, create_and_delete_user):
        token = create_and_delete_user[2]
        response = requests.post(Endpoints.create_order,headers={'Authorization': token}, data=Ingredients.burger_wrong_hash)
        assert response.status_code == 500      