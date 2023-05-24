# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('enter number: '))
degree = 0
while 2 ** degree <= n:
    print(2 ** degree, end=' ')
    degree += 1
