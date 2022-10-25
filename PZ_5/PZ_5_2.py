# Вариант 11
# 2. Описать функцию SortInc3(A, B, C), меняющую содержимое переменных А, В, С
# таким образом, чтобы их значения оказались упорядоченными по возрастанию (А,
# В, С — вещественные параметры, являющиеся одновременно входными и
# выходными). С помощью этой функции упорядочить по возрастанию два данных
# набора из трех чисел: (А1, В1, С1) и (А2, В2, С2).

def SortInc3(*args):  # сортировка переданных значений
    return sorted(args)


def try_except():  # обработка исключений
    a = input('Введите вещественное число: ')
    while type(a) != float:
        try:
            a = float(a)
        except ValueError:
            print('Введите вещественный тип числа!')
            a = input()
    return a


A1, B1, C1 = [try_except() for i in range(3)]  # ввод 3 чисел
A2, B2, C2 = [try_except() for x in range(3)]

print('Первый список чисел', *SortInc3(A1, B1, C1))  # вывод списка чисел
print('Второй список чисел', *SortInc3(A2, B2, C2))