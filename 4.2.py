from random import randint
list = [randint(-3, 10) for i in range(5)]
print(list)
new_list = [el for num, el in enumerate(list) if list[num - 1] < list[num]]
print(f"Исходный список: {list}")
print(f"Итоговый список: {new_list}")