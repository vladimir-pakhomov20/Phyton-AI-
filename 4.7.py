def fact(n):
    num = 1
    if n == 0:
        yield f"{n}! = 1"
    for i in range(1, n + 1):
            num *= i
            yield f" {i}! = {num}"
for el in fact(int(input("Введите число: "))):
    print(el)