import requests
from controller.messages import calculate_qid

# get votes
votes = requests.get('http://localhost:8080/votes').json()

# store filtered message id for additional use in questions
filtered_message_id = []


def calculate_mid(filtered_user_id):
    for i in range(len(votes)):
        if votes[i]['userId'] in filtered_user_id:
            filtered_message_id.append(votes[i]['messageId'])
    # pass to questions.py
    calculate_qid(filtered_message_id)

# test
# print(f"Id: {votes[i]['id']}, userId: {votes[i]['userId']}, messageId: {votes[i]['messageId']}, questionId: {votes[i]['questionId']}")