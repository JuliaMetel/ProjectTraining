# Задание 12
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.
def task_12():
    name_file = input('Введите название файла:').split('.')
    try:
        print(name_file[1])
    except IndexError:
        print('Расширение у файла определить невозможно')

