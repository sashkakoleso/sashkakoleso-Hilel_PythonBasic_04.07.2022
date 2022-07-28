def is_palindrome(string: str) -> bool:
    '''
    Функция проверяет, является ли переданная строка палиндромом
    '''
    my_string = ''
    for char in string.lower():
        if char.isalpha():
            my_string += char

    return my_string == my_string[::-1]

print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('OP'))
print(is_palindrome('a'))