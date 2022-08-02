def difference(*args):
    '''
    Функция принимает произвольный набор целых или вещественных чисел
    и возвращает разницу между максимальным и минимальным числом
    '''
    if args:
        return round(max(args) - min(args), 2)
    return 0


print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())
