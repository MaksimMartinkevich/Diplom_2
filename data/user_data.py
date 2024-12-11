import faker

from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'testmail_B2@yandex.ru',
        "password": "password"}

    data_negative = {
        "email": 'testmail_C12345@yandex.ru',
        "password": "password"}

    data_double = {
        "email": 'testmail_B2@yandex.ru',
        "password": "password",
        "name": "Nina"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "Nina"}

    data_without_password = {
        "email": 'testmail_B2@yandex.ru',
        "password": "",
        "name": "Nina"}

    data_without_name = {
        "email": 'testmail_B2@yandex.ru',
        "password": "password",
        "name": ""}

    data_updated = {
        "email": 'testmail_B2@yandex.ru',
        "password": "password",
        "name": "Maks"}
