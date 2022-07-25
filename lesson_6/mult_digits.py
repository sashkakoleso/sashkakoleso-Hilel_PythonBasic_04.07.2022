users_num = int(input())
#users_num = 999
#users_num = 1000
#users_num = 423
#users_num = 1

x = 1

if users_num <= 9:
    print(users_num)
else:
    while users_num :
        last_digit = users_num % 10
        x *= last_digit
        users_num //= 10

        if users_num == 0:
            if x <= 9:
                print(x)
                break
            else:
                users_num = x
                x = 1

