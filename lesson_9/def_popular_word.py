def popular_words(*args) -> dict:
    '''
    Функция принимает на вход два аргумента : строку и список слов.
    Функция возвращает словарь, где ключ - слово из списка, а значение ключа - сколько раз слово встретилось
    в строке.
    '''

    text_list = [word for word in args[0].lower().split()]
    dict_counter = {}

    for i in args[1]:
        dict_counter.setdefault(i, text_list.count(i))

    return dict_counter


print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                    ['i', 'was', 'three', 'near']))