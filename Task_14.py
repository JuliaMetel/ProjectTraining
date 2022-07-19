# Задание 14
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Напишите программу, которая выводит чётные числа из заданного списка
# и останавливается, если встречает число 237.
import random

def task_14():
    var_list = [random.randint(-300,300) for x in range(20)]
    var_list.insert(13,237)
    for x in var_list:
        if x == 237:
            break
        elif x % 2 != 0:
            print(x)


