import requests

questions = requests.get('http://localhost:8080/questions').json()
