users_input = input()
#users_input = 'a-c'
#users_input = 'a-a'
#users_input = 's-H'
#users_input = 'a-A'

range_list = users_input.split('-')

if range_list[0] == range_list[1]:
    print(range_list[0])

elif range_list[0] < range_list[1]:
    for i in range(ord(range_list[0]), ord(range_list[1]) + 1):
        print(chr(i), end='')

else:
    lower = ''
    for i in range(ord(range_list[0]), ord('z') + 1):
        lower += chr(i)

    upper = ''
    for i in range(ord('A'), ord(range_list[1]) + 1):
        upper += chr(i)

    print(lower + upper)

