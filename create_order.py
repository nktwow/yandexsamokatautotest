import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=data.order_body, headers=data.headers)


def get_view_order(track):
    return requests.get(url=f'{configuration.BASE_URL}{configuration.VIEW_ORDER}{track}',
                        json=data.order_body, headers=data.headers)
