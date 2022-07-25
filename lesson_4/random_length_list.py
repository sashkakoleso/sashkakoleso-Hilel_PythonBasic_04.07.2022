from random import randint

lst = [randint(0, 50) for i in range(randint(3, 10))]
#lst = [randint(0, 50) for i in range(randint(3, 10))]
#lst = [randint(0, 50) for i in range(randint(3, 10))]

answer = [lst[0], lst[2], lst[-2]]

print(lst)
print(answer)