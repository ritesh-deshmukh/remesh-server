import requests

votes = requests.get('http://localhost:8080/votes').json()
