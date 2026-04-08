import pytest
from helpers import *
from data import *
import requests


@pytest.fixture()
def create_and_delete_user():
    payload = create_user()
    response = requests.post(Endpoints.create_user, data=payload)
    token = response.json()["accessToken"]
    yield  response, payload, token
    requests.delete(Endpoints.data_user, headers={'Authorization': token})



