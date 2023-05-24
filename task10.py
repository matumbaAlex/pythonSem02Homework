# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('enter quantity coins: '))
countEagle = 0
countTails = 0
for i in range(n):
    temp=int(input('enter Eagle or Tails, Eagle=0,Tails=1: '))
    if temp == 0: countEagle += 1
    else: countTails += 1
if countEagle > countTails: print(f'quantity coins turn over={countTails}')
else : print(f'quantity coins turn over={countEagle}')
