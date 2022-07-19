# Задание 3
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator
def task_3():
    print('Задание 3')
    var_dict = {'key0': 1, 'key1': 45, 'key2': -34, 'key3': -56.45, 'key4': 0}
    print(dict(sorted(var_dict.items(), key=operator.itemgetter(1))))
    print(dict(sorted(var_dict.items(), key=lambda x: x[1])))
    print(dict(sorted(var_dict.items(), key=operator.itemgetter(1), reverse=True)))