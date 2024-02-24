import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH,  # подставляем полный url
                         json=body )

# = post_new_order(data.user_body);
#print(response.status_code, response.json())
#print({"t": response.json()["track"]})
#print(response.url)
def post_orders_track(track):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_TRACK_PATH,
                        params={"t": track } )

#response = post_orders_track();
#print(response.url)
#print(response.status_code, response.json())
