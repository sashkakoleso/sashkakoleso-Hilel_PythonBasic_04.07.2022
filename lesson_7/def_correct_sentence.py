def correct_sentence(string: str) -> str :
    correct_string = list(string)
    if not correct_string[0].isupper():
        correct_string[0] = correct_string[0].upper()

    if not correct_string[-1] == '.':
        correct_string.append('.')

    return ''.join(correct_string)


print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))