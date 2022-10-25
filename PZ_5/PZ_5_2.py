# Вариант 11
# 2. Описать функцию SortInc3(A, B, C), меняющую содержимое переменных А, В, С
# таким образом, чтобы их значения оказались упорядоченными по возрастанию (А,
# В, С — вещественные параметры, являющиеся одновременно входными и
# выходными). С помощью этой функции упорядочить по возрастанию два данных
# набора из трех чисел: (А1, В1, С1) и (А2, В2, С2).


def SortInc3(a, b, c):  # сортировка переданных значений
    if a > c:
        a, c = c, a
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    return a, b, c


def try_except(a):  # обработка исключений
    while type(a) != float:
        try:
            a = float(a)
        except ValueError:
            print('Введите вещественный тип числа!')
            a = input()
    return a


A1, B1, C1 = try_except(input('Введите A1: ')), try_except(input('Введите B1: ')), try_except(input('Введите C1: '))
A2, B2, C2 = try_except(input('Введите A2: ')), try_except(input('Введите B2: ')), try_except(input('Введите C2: '))

print('Первый набор чисел: ', SortInc3(A1, B1, C1))
print('Второй набор чисел: ', SortInc3(A2, B2, C2))
