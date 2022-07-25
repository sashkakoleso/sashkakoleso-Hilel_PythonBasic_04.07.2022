def second_index(string: str, char: str) -> int :
    first_index = string.find(char)
    find_second_index = string.find(char, first_index+1)

    return find_second_index if find_second_index != -1 else None

print(second_index('sims', 's'))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
