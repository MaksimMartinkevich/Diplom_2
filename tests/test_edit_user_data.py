import allure
import requests

from data.endpoints import Urls, Endpoints
from data.user_data import User


@allure.suite('Изменение данных пользовователя')
class TestEditUserData:

    @allure.description("Успешное изменение данных email авторизованного пользователя при попытке изменения")
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_edit_user_email_with_auth(self, create_user):
        payload = {'email': User.create_data_user()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.URL}{Endpoints.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.description("Успешное изменение данных password авторизованного пользователя при попытке изменения")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_edit_user_password_with_auth(self, create_user):
        payload = {'password': User.create_data_user()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.URL}{Endpoints.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Успешное изменение данных name авторизованного пользователя при попытке изменения")
    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_edit_user_name_with_auth(self, create_user):
        payload = {'name': User.create_data_user()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.URL}{Endpoints.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.description("Срабатывание alert при попытке изменения данных неавторизованного пользователя")
    @allure.title("Изменение данных пользователя без авторизацией")
    def test_edit_user_data_not_auth(self):
        r = requests.patch(f"{Urls.URL}{Endpoints.CHANGE_USER_DATA}", data=User.create_data_user())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'
