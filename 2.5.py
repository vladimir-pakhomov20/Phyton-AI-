a = [7, 5, 3, 3, 2]
print(f"Рейтинг: {a}")
b = int(input("Введите число: "))
for i in range(len(a)):
        if a[i] == b:
            a.insert(i + 1, b)
            break
        elif a[0] < b:
            a.insert(0, b)
            break
        elif a[-1] > b:
            a.append(b)
            break
        elif a[i] > b and a[i + 1] < b:
            a.insert(i + 1, b)
            break
print(f"Новый рейтинг - {a}")
