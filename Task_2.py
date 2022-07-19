# Задание 2
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
def task_2():
    print('Задание 2')
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for x in a:
        for y in b:
            if x == y:
                print(x)
    # Filter and lambda-function:
    print(list(filter(lambda x: x in b, a)))
    # List Comprehension:
    print([x for x in a for y in b if x == y])
    # Через множества, но поврорающиеся элементы исключатся
    print(list(set(a) & set(b)))