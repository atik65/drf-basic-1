import requests

endpoint = 'http://0.0.0.0:4000/api/product/create/'

def make_request():
    res = requests.post(endpoint, data={'name': 'Orange juice', 'price': 48})
    print(res.json())


make_request()