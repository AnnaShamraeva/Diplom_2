import pytest
import requests
from helpers import *
from data import EndpointAndUrl

@pytest.fixture(scope="function")
def create_user():
    login_pass = register_new_user() 
    yield login_pass
    r_login = requests.post(EndpointAndUrl.LOGIN_USER, data={
        'email': login_pass[0], 
        'password': login_pass[1]
    })
    token = r_login.json()['accessToken']
    delete_user(token)


