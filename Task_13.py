# Задание 13
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# При заданном целом числе n посчитайте n + nn + nnn.
def task_13(n):
    print(n*123)

def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)