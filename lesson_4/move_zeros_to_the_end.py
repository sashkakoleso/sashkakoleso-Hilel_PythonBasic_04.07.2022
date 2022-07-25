lst = [0, 1, 0, 3, 12]
#lst = [0]
#lst = [1, 0, 3, 0, 0, 0, 5]
#lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

answer = []
zero_lst = []

for value in lst:
    if value == 0:
        zero_lst.append(value)
    else:
        answer.append(value)

answer.extend(zero_lst)

print(answer)