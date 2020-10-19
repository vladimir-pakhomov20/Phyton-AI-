from itertools import cycle

a = int(input(f"Сколько раз тебе повторять, что всё нужно делать вовремя? "))
count = 0
list = ("Всё", "нужно", "делать", "вовремя")
iterator = cycle(list)
for item in cycle(list):
    if count == a * 4:
        break
    print(item)
    count += 1