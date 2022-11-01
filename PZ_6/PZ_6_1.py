def try_except(a):  # обработка исключений
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print('Введите целое число!')
            a = input()
    return a


A = []
N = try_except(input('Введите кол-во элементов списка: '))
i = 1
while i <= N:  # составление списка
    A.append(input('Введите один из элементов списка: '))
    i += 1
print(A[1:N + 1:2])
