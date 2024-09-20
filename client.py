import requests

endpoint = 'http://0.0.0.0:4000/api/product/drf/'

def make_request():
    res = requests.get(endpoint)
    print(res.json())


make_request()