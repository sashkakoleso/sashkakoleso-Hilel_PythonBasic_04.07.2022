users_number = int(input())

digit_5 = users_number % 10
digit_4 = (users_number // 10) % 10
digit_3 = (users_number // 100) % 10
digit_2 = (users_number // 1000) % 10
digit_1 = (users_number // 10000) % 10

reversed_number = (digit_5 * 10000) + (digit_4 * 1000) + (digit_3 * 100) + (digit_2 * 10) + digit_1

print(reversed_number)
