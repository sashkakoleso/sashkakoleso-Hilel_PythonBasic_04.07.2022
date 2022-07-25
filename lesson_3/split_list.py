#чисто для удобства тестирования :)
my_list = list(map(int, input().split()))

#my_list = []
#my_list = [1]
#my_list = [1, 2, 3, 4, 5]
#my_list = [1, 2, 3, 4, 5, 6]

if len(my_list) == 0 :
    split_list = [[], []]
    print(split_list)

elif len(my_list) == 1:
    split_list = []
    split_list.append(my_list)
    split_list.append([])
    print(split_list)

elif len(my_list) > 1 and len(my_list) % 2 == 0:
    split_list = []
    first_half = my_list[ : int(len(my_list) / 2)]
    split_list.append(first_half)

    second_half = my_list[int(len(my_list) / 2) : ]
    split_list.append(second_half)
    print(split_list)

else:
    split_list = []
    split_list.append(my_list[ : int(len(my_list) / 2) + 1])
    split_list.append(my_list[int(len(my_list) / 2) + 1 : ])
    print(split_list)