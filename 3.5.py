def sum():
    sum_res = 0
    b = False
    while b == False:
        number = input("Введите числа или нажмите Q для выхода из программы: ").split()
        res = 0
        for el in range(len(number)):
            if number[el] == "q" or number[el] == "Q":
                b = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Сумма чисел: {res}")
        print(f"Итоговая сумма чисел: {sum_res}")

sum()