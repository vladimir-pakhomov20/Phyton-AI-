arg1 = int(input("Число 1: "))
arg2 = int(input("Число 2: "))
arg3 = int(input("Число 3: "))

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print( my_func(arg1 , arg2, arg3))