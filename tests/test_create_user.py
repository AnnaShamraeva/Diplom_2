import pytest
import allure
import requests
from data import Message, EndpointAndUrl
from helpers import *



class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя POST запрос /api/auth/register')
    def test_create_user(self):
        email, password, name = generate_data()
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        response = requests.post(EndpointAndUrl.CREATE_USER, data = payload)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание пользователя, который уже зарегистрирован POST запрос /api/auth/register')
    def test_create_two_identical_user(self):
        login_pass = register_new_user()
        response = requests.post(EndpointAndUrl.CREATE_USER, data = {
            'email': login_pass[0],
            'password': login_pass[1],
            'name': login_pass[2]
        })
        assert response.status_code == 403
        assert response.json()['success'] is False
        assert response.json()['message'] == Message.USER_ALREADY_EXISTS


    @allure.title('Cоздать пользователя и не заполнить одно из обязательных полей POST запрос /api/auth/register')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_create_user_whithout_email_or_password(self, field):
        payload = generate_data_payload()
        del payload[field]
        response = requests.post(EndpointAndUrl.CREATE_USER, data = payload)
        assert response.status_code == 403
        assert response.json()['success'] is False
        assert response.json()['message'] == Message.USER_WITHOUT_DATA

    