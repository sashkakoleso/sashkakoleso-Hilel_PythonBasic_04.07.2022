lst = [0, 1, 2, 3, 4, 5]
#lst = [1, 3, 5]
#lst = [6]
#lst = []

sum_even_indx = 0

if len(lst) == 0:
    print(0)
else:
    for indx, value in enumerate(lst):
        if indx % 2 == 0:
            sum_even_indx += value
    answer = sum_even_indx * lst[-1]
    print(answer)
