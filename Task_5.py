# Задание 5
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
def task_5():
    print('Задание 5')
    var_dict = {'key0': 1, 'key1': 45, 'key2': -34, 'key3': -56.45, 'key4': 0}
    var_dict4 = dict(sorted(var_dict.items(), key=lambda x: x[1], reverse=True)[:3])
    print(list(var_dict4.keys()))