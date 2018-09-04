import requests
from compute.users import age,sex,income,livingEnvironment

users = requests.get('http://localhost:8080/users').json()
votes = requests.get('http://localhost:8080/votes').json()
messages = requests.get('http://localhost:8080/messages').json()
questions = requests.get('http://localhost:8080/questions').json()
# print(len(messages))

filtered_users = []
filtered_votes = []
filtered_messages = []

for i in range(len(users)):
    if \
            users[i]['sex'] == 'M' and \
            users[i]['age'] == '18-24' and \
            users[i]['income'] == '<20,000' and \
            (users[i]['livingEnvironment'] == 'Urban' or users[i]['livingEnvironment'] == 'Rural'):
                # print(f"id: {users[i]['id']}")
                filtered_users.append(users[i]['id'])


for i in range(len(votes)):
    if votes[i]['userId'] in filtered_users:
        filtered_votes.append(votes[i]['messageId'])
        # print(f"Id: {votes[i]['id']}, userId: {votes[i]['userId']}, messageId: {votes[i]['messageId']}, questionId: {votes[i]['questionId']}")


for i in range(len(messages)):
    if messages[i]['id'] in filtered_votes:
        filtered_messages.append(messages[i]['questionId'])
        # print(f"Message(answer) text: {messages[i]['text']}")

for i in range(len(questions)):
    if questions[i]['id'] in filtered_messages:
        print(f"Question text: {questions[i]['text']}")
# print(count)
# print(filtered_votes)
# print(answer)
# print(age(users))