# Дан список размера N, все элементы которого, кроме последнего,
# упорядочены по возрастанию. Сделать список упорядоченным,
# переместив последний элемент на новую позицию.

import random
def PrintList(List):
    for element in List:
        print(element, end=' ')
    print()
ListSort = []
n = int(input('Введите размер списка: '))
t = 0
while t < n - 1:
    ListSort.append(random.randint(-100, 100))
    t += 1
ListSort.sort()
ListSort.append(random.randint(-100, 100))
print('Исходный список:', sep='\n')
PrintList(ListSort)

x = ListSort[n - 1]
i = n - 2
while i >= 0 and ListSort[i] > x:
    ListSort[i + 1] = ListSort[i]
    i -= 1
ListSort[i + 1] = x
print('Упорядоченный список:', sep='\n')
PrintList(ListSort)
