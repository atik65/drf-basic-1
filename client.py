import requests

endpoint = 'http://0.0.0.0:4000/api/product/create/'

def create_request():
    res = requests.post(endpoint, data={'name': 'Orange juice', 'price': 48})
    print(res.json())


def get_request():
    endpoint = 'http://0.0.0.0:4000/api/product/details/1/'
    res = requests.get(endpoint)
    print(res.json())


get_request()
# create_request()