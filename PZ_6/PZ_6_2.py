# Дан целочисленный список размера N.
# Найти количество различных элементов в данном списке.

import random
def PrintList(ListAppend):
    for element in ListAppend:
        print(element, end=' ')
    print()
ListDiff = []
n = int(input('Введите размер списка: '))
t = 0
while t < n:
    ListDiff.append(random.randint(-100, 100))
    t += 1
print('Исходный список', sep='\n')
PrintList(ListDiff)
unique = []
t = 0
while t < len(ListDiff):
    if ListDiff[t] not in unique:
        unique.append(ListDiff[t])
    t += 1
print('Количество различных элементов: ', len(unique), sep='\n')
