import requests

users = requests.get('http://localhost:8080/users').json()
questions = requests.get('http://localhost:8080/questions').json()
messages = requests.get('http://localhost:8080/messages').json()
votes = requests.get('http://localhost:8080/votes').json()

income1 = int(users[0]['income'].split("-")[0].replace(',','').replace('+','').replace('<',''))
income2 = int(users[0]['income'].split("-")[1].replace(',','').replace('+','').replace('<',''))
age1 = int(users[22]['age'].split("-")[0].replace(',','').replace('+','').replace('<',''))
age2 = int(users[22]['age'].split("-")[1].replace(',','').replace('+','').replace('<',''))
print(income1,income2)
print(age1,age2)
count = 0
for i in range(len(users)):
    if int(users[i]['income'].split("-")[0].replace(',','').replace('+','').replace('<','')) == 100000:
        count += 1
        print(users[i]['id'])
print(count)
