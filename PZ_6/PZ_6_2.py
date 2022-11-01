import random


def try_except_int(a):  # обработка исключений на int
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print('Введите целое число!')
            a = input()
    return a


def try_except_float(a):  # обработка исключений на float
    while type(a) != float:
        try:
            a = float(a)
        except ValueError:
            print('Введите число!')
            a = input()
    return a


def spisok(a, b):
    x = 0
    lst = []
    while x != a:
        lst.append(random.randrange(0, b))
        x += 1
    return lst


N = try_except_int(input('Введите кол-во элементов списка: '))
Z = try_except_float(input('Список будет формироваться с 0 и до '))
R = try_except_float(input('Введите число R: '))
lst = spisok(N, Z)

i = 0
result = Z
result_number = 0
while i != N:
    if abs(lst[i] - R) > result:
        result = abs(lst[i] - R)
        result_number = lst[i]
        i += 1
    else:
        i += 1

print('Список:', lst)
print('Элемент списка наиболее близкий к R: ', result_number)

# dodelat!
