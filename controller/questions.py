import requests

questions_file = open('questions_data.txt','w')
questions = requests.get('http://localhost:8080/questions').json()


def questions_perId(filtered_question_id):
    print("List of Questions:\n")
    count = 0
    for i in range(len(questions)):
        if questions[i]['id'] in filtered_question_id:
            count += 1
            print(f"Question text {count}: {questions[i]['text']}\n")
            questions_file.write(f"Question text {count}: {questions[i]['text']}\n")