def find_unique_value(list_of_digits: list):
    '''
    Функция принимает как аргумент список и возваращает уникальное число из него
    '''

    d = {}
    for n in list_of_digits:
        d.setdefault(n, 0)
        d[n] += 1

    for key, value in d.items():
        if value == 1:
            return key


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))