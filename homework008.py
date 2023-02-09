import re
text_to_search = '''
#ABCDEF
“2*9-6*5” или (3+5)-(9*4)
"Завтрак в 09:00" "37:98" "23:67" "123:12" "12:623" "213:123" 
Часы и время:
завтрак 9:12 9:88 33:15
обед 12:59 14:78 27:15
ужин 18:47 00:05
Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.

Написать регулярное выражение для определения эстонского личного кода (ID_Code)
'''
# 1
# pattern = re.compile(r'(#[0-F]{6})')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# 2
# pattern = re.compile(r'(\d)[^+]')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# 3
# pattern = re.compile(r'([0-1][0-9]|[2][0-3]):([0-5][0-9])')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# 4
# with open('files/people.txt', 'r', encoding='utf8') as file:
#     people_data = file.read()
#
# name_and_surname= []
# address = []
# pattern = re.compile(r'(\d{3} ).+\w+')
# matches = pattern.finditer(people_data)
# for match in matches:
#     address.append(match.group())
# print(address)














