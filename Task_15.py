# Задание 15
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

def task_15():
    var_list1 = input('Введите первый список через пробел: ').split(' ')
    var_list2 = input('Введите первый список через пробел: ').split(' ')
    result = list(filter(lambda x: x not in var_list2,var_list1))
    print(result)