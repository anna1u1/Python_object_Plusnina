# Дан список размера N и целые числа K и L (1 < K < L < N).
# Найти сумму элементов списка с номерами от K до L включительно.

import random

def PrintList(List):
    for element in List:
        print(element, end=' ')
    print()


ListSum = []
n = int(input('Введите размер списка: '))

t = 0
while t < n:
    ListSum.append(random.randint(-100, 100))
    t += 1

print('Исходный список:', sep='\n')
PrintList(ListSum)

k = int(input('Введите K: '))
l = int(input('Введите L: '))

s = 0
i = k
while i <= l:
    s += ListSum[i]
    i += 1

print('Сумма элементов с номерами от K до L: ', s)