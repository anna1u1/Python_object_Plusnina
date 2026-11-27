# Дан список размера N и целые числа K и L (1 < K < L < N).
# Найти сумму элементов списка с номерами от K до L включительно.

import random

def PrintList(ListAppend):
    for element in ListAppend:
        print(element, end=' ')
    print()
ListSum = []
n = int(input('Введите размер списка: '))
t = 0
while t < n:
    ListSum.append(random.randint(-100, 100))
    t += 1
print('Исходный список', sep='\n')
PrintList(ListSum)
k = int(input('Введите K: '))
l = int(input('Введите L: '))
s = 0
t = k
while t <= l:
    s += ListSum[t - 1]
    t += 1

print('Сумма элементов с номерами от K до L: ', s, sep='\n')
