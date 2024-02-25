import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH,  # подставляем полный url
                         json=body )

def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK_PATH,
                        params={"t": track } )

