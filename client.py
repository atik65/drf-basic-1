import requests

endpoint = 'http://0.0.0.0:4000'

def make_request():
    res = requests.get(endpoint, params={'q': 'hello', 'foo': 'bar'})
    print(res.json())


make_request()