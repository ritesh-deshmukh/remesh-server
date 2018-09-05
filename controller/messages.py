import requests
from controller.questions import questions_perId

messages = requests.get('http://localhost:8080/messages').json()
questions = requests.get('http://localhost:8080/questions').json()

filtered_question_id = []


def calculate_qid(filtered_message_id):
    print("Messages voted by users that satisfy the parameters you provided: \n")
    for i in range(len(messages)):
        if messages[i]['id'] in filtered_message_id:
            filtered_question_id.append(messages[i]['questionId'])
            print(f"User id: {messages[i]['creatorId']},\n"
                  f"Answered to question: {questions[int(messages[i]['questionId'])-1]['text']}\n"
                  f"With Message text: {messages[i]['text']},\n")

    print("\n")
    questions_perId(filtered_question_id)
