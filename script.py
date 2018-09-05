# import requests

from controller.users import calculate_uid

# users = requests.get('http://localhost:8080/users').json()
# votes = requests.get('http://localhost:8080/votes').json()
# messages = requests.get('http://localhost:8080/messages').json()
# questions = requests.get('http://localhost:8080/questions').json()
# print(len(messages))

# filtered_user_id = []
# filtered_message_id = []
# filtered_question_id = []


# print("Filter Remesh DB")
# print("Enter sex choice: F, M")
# sex_input = input("Enter user sex: ")
sex_input = 'M'

# print("Age range choice: 1->40-49, 2->50-59, 3->65+, 4->30-39, 5->18-24, 6->25-29, 7->60-64")
# age_input = input("Enter age range: ")
age_input = '18-24'

# print("Income range choice: 1->90,000-100,000, 2->60,000-70,000, 3->30,000-40,000, \n"
#       "4. <20,000, 5. 80,000-90,000, 6. 70,000-80,000, 7. 100,000+, \n"
#       "8. 50,000-60,000, 9. 20,000-30,000, 10. 40,000-50,000")
# income_input = input("Enter income range: ")
income_input = '<20,000'

# print("Living Environment choice: 'Urban', 'Suburban', 'Rural'")
# livEnv_input = input("Enter Living Enviroment: ")
livEnv_input = 'Urban'

calculate_uid(sex_input,age_input,income_input,livEnv_input)

# print("Filter Remesh DB")
# print("Enter sex choice: F, M")
# sex_input = input("Enter user sex: ")
# print("Age range choice: 1->40-49, 2->50-59, 3->65+, 4->30-39, 5->18-24, 6->25-29, 7->60-64")
# age_input = input("Enter age range: ")
# print("Income range choice: 1->90,000-100,000, 2->60,000-70,000, 3->30,000-40,000, \n"
#                             "4. <20,000, 5. 80,000-90,000, 6. 70,000-80,000, 7. 100,000+, \n"
#                             "8. 50,000-60,000, 9. 20,000-30,000, 10. 40,000-50,000")
# income_input = input("Enter income range: ")
# print("Living Environment choice: 'Urban', 'Suburban', 'Rural'")
# livEnv_input = input("Enter Living Enviroment: ")

# for i in range(len(users)):
#     if \
#             users[i]['sex'] == sex_input and \
#             users[i]['age'] == age_input and \
#             users[i]['income'] == income_input and \
#             (users[i]['livingEnvironment'] == livEnv_input):
#                 # print(f"id: {users[i]['id']}")
#                 filtered_user_id.append(users[i]['id'])

#
# for i in range(len(votes)):
#     if votes[i]['userId'] in filtered_user_id:
#         filtered_message_id.append(votes[i]['messageId'])
#         # print(f"Id: {votes[i]['id']}, userId: {votes[i]['userId']}, messageId: {votes[i]['messageId']}, questionId: {votes[i]['questionId']}")


# for i in range(len(messages)):
#     if messages[i]['id'] in filtered_message_id:
#         filtered_question_id.append(messages[i]['questionId'])
#         # print(f"Message(answer) text: {messages[i]['text']}")


# count = 0
# for i in range(len(questions)):
#     if questions[i]['id'] in filtered_question_id:
#         count += 1
#         print(f"Question text {count}: {questions[i]['text']}")


# print(count)
# print(filtered_votes)
# print(answer)
# print(age(users))