# Дан целочисленный список размера N.
# Найти количество различных элементов в данном списке.

import random

def PrintList(List):
    for element in List:
        print(element, end=' ')
    print()


ListDiff = []
n = int(input('Введите размер списка: '))
t = 0
while t < n:
    ListDiff.append(random.randint(-100, 100))
    t += 1
print('Исходный список:', sep='\n')
PrintList(ListDiff)
unique = []
for element in ListDiff:
    if element not in unique:
        unique.append(element)
print('Количество различных элементов: ', len(unique))
