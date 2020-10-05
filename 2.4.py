a = input("введите строку ")
b = []
c = 1
for el in range(a.count(" ") + 1):
    b = a.split()
    if len(str(b)) <= 10:
        print(f" {c} {b [el]}")
        c += 1
    else:
        print(f" {c} {b [el] [0:10]}")
        c += 1