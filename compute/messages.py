import requests

messages = requests.get('http://localhost:8080/messages').json()

