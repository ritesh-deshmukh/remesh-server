import requests
# import compute.votes as user_input
from controller.questions import questions_perId

messages = requests.get('http://localhost:8080/messages').json()

filtered_question_id = []

def calculate_qid(filtered_message_id):
    for i in range(len(messages)):
        if messages[i]['id'] in filtered_message_id:
            filtered_question_id.append(messages[i]['questionId'])
            # print(f"Message(answer) text: {messages[i]['text']}")
    questions_perId(filtered_question_id)
