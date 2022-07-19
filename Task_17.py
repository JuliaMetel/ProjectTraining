# Задание 17
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Сложите цифры целого числа.

def task_17():
    var_str = input('Введите целое число: ')
    if (var_str[0] == '-'): var_str = var_str[1:]
    result = 0
    for x in var_str:
        result += int(x)
    print(result)