import requests
from controller.questions import questions_perId

# create file to write messages output
message_file = open('messages_data.txt','w')

# get messages and questions
messages = requests.get('http://localhost:8080/messages').json()
questions = requests.get('http://localhost:8080/questions').json()

# store question id for additional use in questions
filtered_question_id = []


def calculate_qid(filtered_message_id):
    print("Messages voted by users that satisfy the parameters you provided: \n")
    for i in range(len(messages)):
        if messages[i]['id'] in filtered_message_id:
            filtered_question_id.append(messages[i]['questionId'])
            print(f"User id: {messages[i]['creatorId']},\n"
                  f"Answered to question: {questions[int(messages[i]['questionId'])-1]['text']}\n"
                  f"With Message text: {messages[i]['text']},\n")
            message_file.write((f"User id: {messages[i]['creatorId']},\n"
                  f"Answered to question: {questions[int(messages[i]['questionId'])-1]['text']}\n"
                  f"With Message text: {messages[i]['text']},\n"))

    print("\n")
    # pass to questions.py
    questions_perId(filtered_question_id)
