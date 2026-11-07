# Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить
# каждой переменной сумму этих значений, а если равны, то присвоить переменным
# нулевые значения. Вывести новые значения переменных A и B.
A, B = input("Введите значиние A:"), input("Введите значение B:")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели.")
        A = input("Введите значение A:")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Неправильно ввели.")
        B = input("Введите значиние B:")
if A != B:
    total = A + B
    A = total
    B = total
    print(total)
else:
    A = 0
    B = 0
    print(A, B)