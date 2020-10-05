t = []
a = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
b = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1 
    for f in a.keys():
        c = input(f'Введите значение свойства "{f}": ')
        a[f] = int(c) if (f == "цена" or f == "количество") else c
        b[f].append(a[f])
    6end((num, a))
    print(f'\nСтруктура товаров\n {"-" * 30}')
    for key, value in b.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)
