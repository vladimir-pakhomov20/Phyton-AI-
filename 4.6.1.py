from itertools import count

for el in count(int(input("Введите начальное целое число меньше 50: "))):
    if el >= 51:
        break
    else:
        print(el)

