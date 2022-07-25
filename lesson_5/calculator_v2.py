print('Привет, я твой калькулятор!')

while True:

    a = float(input('Введи первое целое число или число с плавающей точкой: '))
    b = float(input('Введи второе целое число или число с плавающей точкой: '))
    operation = input('Что делаем с числами ? Введи оператор (+, -, *, /, //, %): ')

    if operation == '+':
        print(a,'+',b,'=', a + b)

    elif operation == '-':
        print(a,'-',b,'=', a - b)

    elif operation == '*':
        print(a,'*',b,'=', a * b)

    elif operation == '/':
        if b == 0:
            print('На 0 делить нельзя !')
        if b != 0:
            print(a,'/',b,'=', a / b)

    elif operation == '//':
        if b == 0:
            print('На 0 делить нельзя !')
        if b != 0:
            print(a,'//',b,'=', a // b)


    elif operation == '%':
        if b == 0:
            print('На 0 делить нельзя !')
        if b != 0:
            print(a,'%',b,'=', a % b)

    else:
        print('Некорректный оператор, выбери один из доступных !')

    print()
    repeat = input('''Хотите провести ещё одно вычисление ?
Введите "yes" или "y *(eng)" для повтора или любой другой символ для выхода: ''')

    if repeat.lower() not in ('yes', 'y'):
        print('Хорошего дня, до свидания !')
        break