# Задание 1
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
def task_1():
    print('Задание 1')
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for x in a:
        if x < 5:
            print(x)
    # Filter and lambda-function:
    print(list(filter(lambda x: x < 5, a)))
    # List Comprehension:
    print([x for x in a if x < 5])