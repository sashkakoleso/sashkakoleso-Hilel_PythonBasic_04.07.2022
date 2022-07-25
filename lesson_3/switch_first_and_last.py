#чисто для удобства тестирования :)
my_list = list(map(int, input().split()))

#my_list = []
#my_list = [1]
#my_list = [12, 3, 4, 10]

if len(my_list) in (0, 1):
    print(my_list)

else:
    x = my_list.pop()
    my_list.insert(0, x)
    print(my_list)