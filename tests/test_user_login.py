import allure
import requests
from data import Message, EndpointAndUrl
from helpers import *
from conftest import create_user

class TestUserAuthorization:
    @allure.title('Вход под существующим пользователем POST запрос /api/auth/login')
    def test_user_authorization(self, create_user):
        login_pass = create_user
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        })
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Вход с неверным логином email POST запрос /api/auth/login')
    def test_user_authorization_with_wrong_email(self, create_user):
        login_pass = create_user
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': 'wrongemail',
            'password': login_pass[1]
        })
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Message.INCORRECT_DATA

    @allure.title('Вход с неверным паролем POST запрос /api/auth/login')
    def test_user_autorization_with_wrong_password(self, create_user):
        login_pass = create_user
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': login_pass[0],
            'password': 'wrongpassword'
        })
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Message.INCORRECT_DATA

    