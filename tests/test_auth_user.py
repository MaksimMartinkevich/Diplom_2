import allure
import requests

from data.endpoints import Urls, Endpoints
from data.user_data import User


@allure.suite('Авторизация пользователя')
class TestAuth:

    @allure.description('Успешная авторизация для пользователя, который есть в системе')
    @allure.title('Авторизация пользователя, который есть в системе')
    def test_login_user(self):
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('Срабатывание alert для пользователя с невалыдными данными авторизации')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.URL}{Endpoints.LOGIN}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') == False
