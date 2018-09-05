from controller.users import calculate_uid

user_input_file = open('user_input_data.txt','w')
print("Filter Remesh DB\n")
user_input_file.write("Filter Remesh DB\n\n")
# take user input for sex of the user
print("Enter user sex:\n"
                      "Options: 1: 'M',\n"
                      "\t\t 2: 'F'")
user_input_file.write("Enter user sex:\n"
                      "Options: 1: 'M',\n"
                      "\t\t 2: 'F'\n")
sex_input_choice = {
      1: 'M',
      2: 'F'
}
sex_input = int(input("Enter user sex: "))
sex_input = sex_input_choice.get(sex_input,-1)
print(f"Your choice: {sex_input}\n")
user_input_file.write(f"Your choice: {sex_input}\n\n")

# take user input for age of the user
print("Enter user age range:\n"
                      "Options: 1: '18-24',\n"
                      "\t\t 2: '25-29',\n"
                      "\t\t 3: '30-39',\n"
                      "\t\t 4: '40-49',\n"
                      "\t\t 5: '50-59',\n"
                      "\t\t 6: '60-64',\n"
                      "\t\t 7: '65+'\n")
user_input_file.write("Enter user age range:\n"
                      "Options: 1: '18-24',\n"
                      "\t\t 2: '25-29',\n"
                      "\t\t 3: '30-39',\n"
                      "\t\t 4: '40-49',\n"
                      "\t\t 5: '50-59',\n"
                      "\t\t 6: '60-64',\n"
                      "\t\t 7: '65+'\n")
age_input_choice = {
      1: '18-24',
      2: '25-29',
      3: '30-39',
      4: '40-49',
      5: '50-59',
      6: '60-64',
      7: '65+',
}
age_input = int(input("Enter age range: "))
age_input = age_input_choice.get(age_input,-1)
print(f"Your choice: {age_input}\n")
user_input_file.write(f"Your choice: {age_input}\n\n")

# take user input for income of the user
print("Enter user income range:\n"
                      "Options: 1: '<20,000',\n"
                      "\t\t 2: '20,000-30,000',\n"
                      "\t\t 3: '30,000-40,000',\n"
                      "\t\t 4: '40,000-50,000',\n"
                      "\t\t 5: '50,000-60,000',\n"
                      "\t\t 6: '60,000-70,000',\n"
                      "\t\t 7: '70,000-80,000',\n"
                      "\t\t 8: '80,000-90,000',\n"
                      "\t\t 9: '90,000-100,000',\n"
                      "\t\t 10: '100,000+',\n")
user_input_file.write("Enter user income range:\n"
                      "Options: 1: '<20,000',\n"
                      "\t\t 2: '20,000-30,000',\n"
                      "\t\t 3: '30,000-40,000',\n"
                      "\t\t 4: '40,000-50,000',\n"
                      "\t\t 5: '50,000-60,000',\n"
                      "\t\t 6: '60,000-70,000',\n"
                      "\t\t 7: '70,000-80,000',\n"
                      "\t\t 8: '80,000-90,000',\n"
                      "\t\t 9: '90,000-100,000',\n"
                      "\t\t 10: '100,000+',\n")
income_input_choice = {
      1: '<20,000',
      2: '20,000-30,000',
      3: '30,000-40,000',
      4: '40,000-50,000',
      5: '50,000-60,000',
      6: '60,000-70,000',
      7: '70,000-80,000',
      8: '80,000-90,000',
      9: '90,000-100,000',
      10: '100,000+'
}
income_input = int(input("Enter income range: "))
income_input = income_input_choice.get(income_input,-1)
print(f"Your choice: {income_input}\n")
user_input_file.write(f"Your choice: {income_input}\n\n")


# take user input for Living Environment of the user
print("Enter user sex:\n"
                      "Options: 1: 'Urban',\n"
                      "\t\t 2: 'Suburban',\n"
                      "\t\t 3: 'Rural'")
user_input_file.write("Enter user sex:\n"
                      "Options: 1: 'Urban',\n"
                      "\t\t 2: 'Suburban',\n"
                      "\t\t 3: 'Rural'\n")
livEnv_input_choice = {
      1: 'Urban',
      2: 'Suburban',
      3: 'Rural',
}
# print("Living Environment choice: 'Urban', 'Suburban', 'Rural'")
livEnv_input = int(input("Enter Living Enviroment: "))
livEnv_input = livEnv_input_choice.get(livEnv_input,-1)
print(f"Your choice: {livEnv_input}\n")
user_input_file.write(f"Your choice: {livEnv_input}\n\n")
print("------------RESULT------------")
user_input_file.write("Messages are included in messages_data.txt,\n"
                      "Questions are included in questions_data.txt")

calculate_uid(sex_input,age_input,income_input,livEnv_input)
