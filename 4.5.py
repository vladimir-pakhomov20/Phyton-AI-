from functools import reduce
def my_func(num1, num2):
    return num1 * num2
print(f"Все четные числа последовательности 100-1000: {[el for el in range(99, 1001) if el % 2 == 0]}")
print(f"Произведение всех четных чисел последовательности 100-1000: \
{reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}")

