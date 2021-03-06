import requests
from controller.votes import calculate_mid

# get users
users = requests.get('http://localhost:8080/users').json()

# store filtered user id for additional use in votes
filtered_user_id = []


def calculate_uid(sex_input,age_input,income_input,livEnv_input):
    for i in range(len(users)):
        if \
                users[i]['sex'] == sex_input and \
                        users[i]['age'] == age_input and \
                        users[i]['income'] == income_input and \
                        (users[i]['livingEnvironment'] == livEnv_input):

            filtered_user_id.append(users[i]['id'])
    # pass to votes.py
    calculate_mid(filtered_user_id)

# Tests
# print(f"id: {users[i]['id']}")
def age(users):
    age_set = set()
    for i in range(len(users)):
        age_set.add(users[i]['age'])
    print(f"Age Range: {age_set}")
    return list(age_set)


def sex(users):
    sex_set = set()
    for i in range(len(users)):
        sex_set.add(users[i]['sex'])
    print(f"Sex Range: {sex_set}")


def income(users):
    income_set = set()
    for i in range(len(users)):
        income_set.add(users[i]['income'])
    print(f"Income Range: {income_set}")


def livingEnvironment(users):
    livEnv_set = set()
    for i in range(len(users)):
        livEnv_set.add(users[i]['livingEnvironment'])
    print(f"Living Environment Range: {livEnv_set}")

# age(users)
# sex(users)
# income(users)
# livingEnvironment(users)