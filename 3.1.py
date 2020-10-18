def div(*args):
    try:
        arg1 = int(input("Введите число 1: "))
        arg2 = int(input("Введите число 2: "))
        func = arg1 / arg2
    except ValueError:
        return "Ошибка числового формата"
    except ZeroDivisionError:
        return "Ошибка деления на ноль"
    return func
print(f'result  {div()}')