def try_except(a):  # обработка исключений
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print('Введите целое число!')
            a = input()
    return a


lst = []
N = try_except(input('Введите кол-во элементов списка: '))

i = 1
while i <= N:  # составление списка
    lst.append(input('Введите один из элементов списка: '))
    i += 1

print('Исходный список: ', lst)
lst.pop(0)  # удаление 1 элемента и замена последнего
lst[-1] = 0
print('Полученный список: ', lst)
