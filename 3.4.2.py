x = float(input("Введите положительное число (x): "))
y = int(input("Введите отрицательное число (y): "))
def my_func (x, y):
    try:
        if x <= 0:
            return "x должен быть положительным"
        if y >= 0:
            return "y должен быть отрицательным"
        else:
            x ** y
    except ValueError:
        return "Неверный формат числа"
print(my_func(x, y))