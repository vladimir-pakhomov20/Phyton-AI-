a = [7, 5, 3, 3, 2]
b = int(input("Введите число: "))
while True:
    if a.count(b):
        a.insert(a.index(b) + a.count(b), float(b))
    else:
        param = 0
        n_param = 0
        for n, i in enumerate(a):
            if b > i:
               if param < i:
                   param = i
                   n_param = n
            else:
                n_param = n + 1
        a.insert(n_param, b)
    print(f"Новый рейтинг - {a}")
    break
