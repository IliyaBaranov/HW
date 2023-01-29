current_year = 2023
year_of_birth = 1988
my_year = (str(current_year - year_of_birth))
code_1 = '354'
code_3 = 132
user_name = 'John'
user_surname = 'Smith'
x = 152
y = 132
code_2 = (int((x % y * 13) ** 0.5))
code_all = (code_1 + '-' + str(code_2) + '-' + str(code_3))
print('Hello ' + user_name + ' ' + user_surname + '. You are ' + my_year + ' years old. Your secret code is ' + (code_all))
