

class EndpointAndUrl:
    MAIN_PAGE = 'https://stellarburgers.education-services.ru/'
    CREATE_USER = f'{MAIN_PAGE}/api/auth/register' # Создание пользователя POST запрос
    LOGIN_USER = f'{MAIN_PAGE}/api/auth/login' # Для авторизации POST запрос
    DO_ORDER = f'{MAIN_PAGE}/api/orders' # Создание заказа POST запрос
    CHANGE_DATA = f'{MAIN_PAGE}/api/auth/user' 
    # Для получения и обновления информации о пользователе GET запрос

class Message:
    # Создание пользователя
       # создать пользователя, который уже зарегистрирован
    USER_ALREADY_EXISTS = 'User already exists' # Если пользователь существует, вернется код ответа 403 Forbidden
       # создать пользователя и не заполнить одно из обязательных полей
    USER_WITHOUT_DATA = 'Email, password and name are required fields' # код ответа 403 Forbidden
    # Логин пользователя
       # вход с неверным логином и паролем
    INCORRECT_DATA = 'email or password are incorrect' # код ответа 401 Unauthorized
    # Создание заказа
       # с авторизацией
       # без авторизации
    WITHOUT_AUTHORISED = 'You should be authorised' # код ответа 401 Unauthorized
       # без ингредиентов
    ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided' # 400 Bad Request
       
class Order:
    # Создание заказа
      # с ингредиентами
   ORDER_WITH_INGREDIENTS = {
        "ingredients": [
                "61c0c5a71d1f82001bdaaa6c",
                "61c0c5a71d1f82001bdaaa79",
                "61c0c5a71d1f82001bdaaa78",
                "61c0c5a71d1f82001bdaaa79",
                "61c0c5a71d1f82001bdaaa73",
                "61c0c5a71d1f82001bdaaa73"]
       }
      # без ингредиентов
   ORDER_WITHOUT_INGREDIENTS = {
       "ingredients": []
       }
      # с неверным хешем ингредиентов 
   ORDER_WITH_WRONG_HASH_INGREDIENTS = {
       "ingredients": ["invalid_hash_123"]
       }
   


