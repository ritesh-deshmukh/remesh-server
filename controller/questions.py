import requests
# import compute.messages as user_input


questions = requests.get('http://localhost:8080/questions').json()

def questions_perId(filtered_question_id):
    count = 0
    for i in range(len(questions)):
        if questions[i]['id'] in filtered_question_id:
            count += 1
            print(f"Question text {count}: {questions[i]['text']}")