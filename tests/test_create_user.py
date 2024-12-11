import pytest
import allure
import requests

from data.endpoints import Urls, Endpoints
from data.user_data import User


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.description('Успешное создание нового пользователя')
    @allure.title('Создание нового пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_USER}', data=User.create_data_user())
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.description('Срабатывание alert при попытке создать существуюшего пользователя')
    @allure.title('Создание пользователя который уже есть в системе')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_USER}', data=User.data_double)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('Срабатывание alert при создании пользователя с невалидными данными')
    @allure.title('Создание пользователя с невалидными данными/незаполненными обязательными полями')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.URL}{Endpoints.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text
