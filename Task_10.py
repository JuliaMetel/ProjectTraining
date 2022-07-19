# Задание 10
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.
def task_10():
    print('Задание 10')
    var_input = input('Введите числа через запятую:').split(',')
    print(list(map(int,var_input)))
    print(tuple(map(int,var_input)))