# Задание 18
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Посчитайте, сколько раз символ встречается в строке.

def task_18(symbol):
    var_str = 'Это строчка для проверки! Она короткая, но информативная:)'
    count = 0
    for x in var_str:
        if x == symbol:
            count +=1
    print(count)
    print(var_str.count(symbol))
