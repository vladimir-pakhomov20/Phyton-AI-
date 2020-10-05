a = input("Введите список значений через пробел ")
b = a.split(" ")
j = 0
for j in range(1, len(b), 2):
    b[j - 1], b[j] = b[j], b[j - 1]
print(b)