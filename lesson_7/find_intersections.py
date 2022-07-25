from random import randint

lst1 = [i for i in range(1, randint(0, 100)) if i % 3 == 0]
lst2 = [i for i in range(1, randint(0, 100)) if i % 5 == 0]

print(lst1)
print(lst2)
myset1 = set(lst1)
myset2 = set(lst2)

print(list(myset1.intersection(myset2)))