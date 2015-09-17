import requests
headers = {'content-type': 'application/json'}
print requests.get('http://127.0.0.1:8000', headers=headers).text
