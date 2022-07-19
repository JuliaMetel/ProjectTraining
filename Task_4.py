# Задание 4
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Напишите программу для слияния нескольких словарей в один.
def task_4():
    print('Задание 4')
    var_dict = {'key0': 1, 'key1': 45, 'key2': -34, 'key3': -56.45, 'key4': 0}
    var_dict2 = {'key5': 15, 'key6': 5, 'key1': -74, 'key8': -6.5, 'key4': 10}
    var_dict3 = dict()
    for x in var_dict,var_dict2:
        var_dict3.update(x)
    print(var_dict3)