# Вариант №11
# 1. Дано целое число N (>0). Найти произведение 1.1 * 1.2 * 1.3 *... (N сомножителей).

N = input('Введите число: ')

while type(N) != int:  # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число')
        N = input()

result = 1.1
k = 1.2
if N > 0:
    while N != 1:  # считаем результат
        result = result * k
        k += 0.1
        N -= 1
    print('Результат:', result)
else:
    print('Число не входит в диапазон!')
