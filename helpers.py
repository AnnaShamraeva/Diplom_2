import allure
import requests

from data import EndpointAndUrl
from faker import Faker

fake = Faker()


# генерируем email, пароль и имя клиента
def generate_data(): 
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return email, password, name

# собираем тело запроса
def generate_data_payload():
    email, password, name = generate_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

@allure.step("Регестрация нового пользователя")
# метод регистрации нового пользователя возвращает список из email, имени и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_user():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    payload = generate_data_payload()
    response = requests.post(EndpointAndUrl.CREATE_USER, data=payload)
    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль клиента
    if response.status_code == 200:
        login_pass.append(payload['email'])
        login_pass.append(payload['password'])
        login_pass.append(payload['name'])
    return login_pass  # возвращаем список

@allure.step('Логин пользователя') 
def login_user():
    login_pass = register_new_user()
    payload = {
        'email': login_pass[0],
        'password': login_pass[1]
    }
    response = requests.post(EndpointAndUrl.LOGIN_USER, data=payload) 
    return response

@allure.step('Получение токена')
def get_token():
    login = login_user()
    token = login.json()['accessToken']
    return token



@allure.step("Удаление пользователя")
def delete_user(token):
    token = get_token()
    headers = {'Authorization': token}
    response = requests.delete(EndpointAndUrl.CHANGE_DATA, headers=headers)


@allure.step('Создание заказа')
def create_order(data):
    response = requests.post(EndpointAndUrl.DO_ORDER, json=data)
    return response



  



