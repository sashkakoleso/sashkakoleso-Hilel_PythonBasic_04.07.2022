def add_one(lst_number: list) -> list:
    '''
    Функция собирает целое число из элементов списка,
    прибавляет 1 к этому число и разбивает обратно в список
    '''

    lst_number = [str(i) for i in lst_number]
    number = int(''.join(lst_number)) + 1
    answer = [int(i) for i in str(number)]
    return answer


print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9, 9]))
print(add_one([0]))
print(add_one([9]))