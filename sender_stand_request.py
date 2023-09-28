import configuration
import data
import requests


def post_new_order(body):
    """ Функция отправляет запрос на создание заказа."""
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)


def get_new_order_track():
    """ Функция для получения номера заказа."""
    responce = post_new_order(data.order_body)
    track = responce.json()['track']
    return track


def get_order():
    """ Функция отправляет запрос на получение заказа по номеру."""
    return requests.get(
        configuration.URL_SERVICE + configuration.TAKE_ORDERS_PATH,params={"t":get_new_order_track()})
responce = get_order()


