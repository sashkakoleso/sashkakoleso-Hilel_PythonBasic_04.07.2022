users_number = int(input())
#users_number = 0
#users_number = 224930
#users_number = 466289
#users_number = 22493
#users_number = 7948799 

if not 0 <= users_number <= 8639999:
    print('Введено некорректне число, перезапустите программу и введите число от 0 до 8639999')

seconds_in_day = 86400
seconds_in_hour = 3600

days = users_number // seconds_in_day
hours = str((users_number % seconds_in_day) // seconds_in_hour).rjust(2, '0')
minutes = str(((users_number % seconds_in_day) % seconds_in_hour) // 60).rjust(2, '0')
seconds = str(users_number % 60).rjust(2, '0')

if days in range(1,101, 20):
    days_word = 'день'
elif days in (2, 3, 4) or days in range(2,101,20) or days in range(3,101,20) or days in range(4,101,20):
    days_word = 'дня'
else:
    days_word = 'дней'

print(f'{days} {days_word}, {hours}:{minutes}:{seconds}')

