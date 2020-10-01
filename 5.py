vir = int(input("Введите выручку: "))
izd = int(input("Введите издержки: "))
if vir - izd > 0:
    prib = int(vir - izd)
    print("Прибыль предприятия составляет ", prib)
    print('Рентабильность предприятия ', prib / vir)
    sot = int(input("Введите количество сотрудников:"))
    print("Прибыль на одного сотрудника составляет", prib / sot)
if vir - izd < 0:
    ubit = int(vir - izd)
    print("Убыток предприятия составляет ", ubit)
if vir - izd == 0:
    print("Сир, всё напрасно, казна пуста!")