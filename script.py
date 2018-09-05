from controller.users import calculate_uid


print("Filter Remesh DB")

# take user input for sex of the user
print("Enter sex choice: F, M")
sex_input_choice = {
      1: 'M',
      2: 'F'
}
sex_input = int(input("Enter user sex: "))
sex_input = sex_input_choice.get(sex_input,-1)
print(f"Your choice: {sex_input}\n")

# take user input for age of the user
print("Age range choice: 1->40-49, 2->50-59, 3->65+, 4->30-39, 5->18-24, 6->25-29, 7->60-64")
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

# take user input for income of the user
print("Income range choice: 1->90,000-100,000, 2->60,000-70,000, 3->30,000-40,000, \n"
      "4. <20,000, 5. 80,000-90,000, 6. 70,000-80,000, 7. 100,000+, \n"
      "8. 50,000-60,000, 9. 20,000-30,000, 10. 40,000-50,000")
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


# take user input for Living Environment of the user
livEnv_input_choice = {
      1: 'Urban',
      2: 'Suburban',
      3: 'Rural',
}
print("Living Environment choice: 'Urban', 'Suburban', 'Rural'")
livEnv_input = int(input("Enter Living Enviroment: "))
livEnv_input = livEnv_input_choice.get(livEnv_input,-1)
print(f"Your choice: {livEnv_input}\n")
print("------------RESULT------------")

calculate_uid(sex_input,age_input,income_input,livEnv_input)
