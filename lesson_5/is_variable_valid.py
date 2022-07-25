from string import ascii_letters, digits
from keyword import kwlist

valid_chars = ascii_letters + digits + '_'

users_var = input('Введите желаемое имя переменной: ')
#users_var = '_'
#users_var = 'x'
#users_var = 'get_value'
#users_var = 'Get_value'
#users_var = 'get_Value'
#users_var = 'getValue'
#users_var = '3m'

flag = True

while len(users_var) == 0:
    print('Название переменной должно содержать хотя бы один символ!')
    users_var = input('Введите желаемое имя переменной: ')

for char in users_var:               # проверка на недопустимые символы
    if char not in valid_chars:
        flag = False
        break

if users_var in kwlist:             # проверка на совпадение с зарезервированными именами
    flag = False

if not users_var.islower():         # проверка на наличие заглавных букв
    flag = False

if users_var.isdigit():             # состоит ли имя переменой только из цифр
    flag = False

if users_var[0].isdigit():          # первый символ цифра ?
    flag = False

if users_var == '_':
    flag = True

print(flag)