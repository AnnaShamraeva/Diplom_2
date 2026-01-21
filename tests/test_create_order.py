import allure
import requests
from data import Message, Order
from helpers import *
from conftest import create_user

class TestDoOrder:
    @allure.step('Сделать заказ с авторизацией')
    def test_do_order_with_login(self, create_user):
        login_pass = create_user
        
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        }) # aвторизация

        order = create_order(Order.ORDER_WITH_INGREDIENTS)
        assert order.status_code == 200
        assert order.json()['success'] is True

    @allure.step('Сделать заказ без авторизации')
    def test_do_order_without_login(self):
        order = create_order(Order.ORDER_WITH_INGREDIENTS)
        assert order.status_code == 200
        assert order.json()['success'] is True


    @allure.step('Сделать заказ с ингредиентами') 
    def test_do_order_with_ingredients(self, create_user):
        login_pass = create_user
        
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        }) # aвторизация

        order = create_order(Order.ORDER_WITH_INGREDIENTS)       
        assert order.status_code == 200
        assert order.json()['success'] is True

    @allure.step('Сделать заказ без ингредиентов')
    def test_do_order_without_ingredients(self, create_user):
        login_pass = create_user
        
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        }) # aвторизация

        order = create_order(Order.ORDER_WITHOUT_INGREDIENTS)
        assert order.status_code == 400 
        assert order.json()['success'] is False
        assert order.json()['message'] == Message.ORDER_WITHOUT_INGREDIENTS

    @allure.step('Сделать заказ с неверным хешем ингредиентов')
    def test_do_order_with_wrong_hash(self, create_user):
        login_pass = create_user
        
        response = requests.post(EndpointAndUrl.LOGIN_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        }) # aвторизация

        order = create_order(Order.ORDER_WITH_WRONG_HASH_INGREDIENTS)
        assert order.status_code == 500
       


