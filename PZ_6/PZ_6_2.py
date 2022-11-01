import random


def try_except(a, b):  # обработка исключений на int или float
    if b == int:
        while type(a) != int:
            try:
                a = int(a)
            except ValueError:
                print('Введите целое число!')
                a = input()
    else:
        while type(a) != float:
            try:
                a = float(a)
            except ValueError:
                print('Введите число!')
                a = input()
    return a


def listing(a, b):  # составление списка со случайными числами
    x = 0
    c = []
    while x != a:
        c.append(random.randrange(0, b))
        x += 1
    return c


N = try_except(input('Введите кол-во элементов списка: '), int)
Z = try_except(input('Список будет формироваться из диапазона с 0 и до '), int)
R = try_except(input('Введите число R: '), float)
lst = listing(N, Z)  # формирование списка чисел

result = lst[0]
result_number = lst[0]
for i in lst:
    if abs(i - R) < abs(result_number - R):
        result = abs(i - R)
        result_number = i

print(f'Список: {lst}')
print(f'Элемент списка наиболее близкий к {R}: {result_number}')
