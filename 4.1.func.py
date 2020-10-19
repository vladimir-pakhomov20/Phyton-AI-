def zp():
    try:
        time = int(input("Введите количество отработанных часов: "))
        rate = int(input("Введите почасовую ставку: "))
        bonus = int(input("Введите размер бонуса сотрудника: "))
        res = time * rate + bonus
        print(f"Заработная плата сотрудника составит: {res} рублей")
    except ValueError:
        print("Только числовые значения!")
zp()