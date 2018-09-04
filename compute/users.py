import requests

users = requests.get('http://localhost:8080/users').json()
count_users = len(users)

def age(users):
    age_set = set()
    for i in range(count_users):
        age_set.add(users[i]['age'])
    print(f"Age Range: {age_set}")


def sex(users):
    sex_set = set()
    for i in range(count_users):
        sex_set.add(users[i]['sex'])
    print(f"Sex Range: {sex_set}")


def income(users):
    income_set = set()
    for i in range(count_users):
        income_set.add(users[i]['income'])
    print(f"Income Range: {income_set}")


def livingEnvironment(users):
    livEnv_set = set()
    for i in range(count_users):
        livEnv_set.add(users[i]['livingEnvironment'])
    print(f"Living Environment Range: {livEnv_set}")

age(users)
sex(users)
income(users)
livingEnvironment(users)
