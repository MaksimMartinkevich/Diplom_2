class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'


class Endpoints:
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    HEADERS = {"Content-Type": "application/json"}