from random import randint
list = [randint(-5, 5) for i in range(10)]
print(list)
new_list = [el for el in list if list.count(el) < 2]
print(new_list)