from random import randint

set_3 = set([i for i in range(1, randint(0, 100)) if i % 3 == 0])
set_5 = set([i for i in range(1, randint(0, 100)) if i % 5 == 0])

#print(set_3)
#print(set_5)

print(list(set_3.intersection(set_5)))