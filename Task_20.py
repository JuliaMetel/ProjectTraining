# Задание 20
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# С помощью анонимной функции извлеките из списка числа, делимые на 15.
import random

def task_20():
    var_list = [random.randint(-100,100) for x in range(100)]
    result = list(filter(lambda x: x % 15 == 0,var_list))
    print(result)