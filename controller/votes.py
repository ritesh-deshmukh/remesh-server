import requests
from controller.messages import calculate_qid

votes = requests.get('http://localhost:8080/votes').json()

filtered_message_id = []

def calculate_mid(filtered_user_id):
    for i in range(len(votes)):
        if votes[i]['userId'] in filtered_user_id:
            filtered_message_id.append(votes[i]['messageId'])
            # print(f"Id: {votes[i]['id']}, userId: {votes[i]['userId']}, messageId: {votes[i]['messageId']}, questionId: {votes[i]['questionId']}")
    calculate_qid(filtered_message_id)
            # return filtered_message_id