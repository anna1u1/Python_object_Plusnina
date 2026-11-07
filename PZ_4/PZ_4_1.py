# Дано вещественное число X и целое число N (> 0). Найти значение выражения X -
# X 3 /(3!) + X5 /(5!) - ... + (-1)N -X
# 2-N+1/((2-N+1)!) (N! = 12 ...N). Полученное число
# является приближенным значением функции sin в точке X.

x = input("Введите вещественное число x:")
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("Неправильно ввели.")
        x = input("Введите вещественное число x:")
N = input("Введите целое число N (> 0):")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели.")
        N = input("Введите целое число N (> 0):")
result = 0.0
i = 0
while i <= N:
    power = 2 * i + 1
    fact = 1
    step = 1
    while step <= power: #факториал
        fact *= step
        step += 1
    term = x ** power / fact
    if i % 2 == 0:
        result += term
    else:
        result -= term
    i += 1
print("Значение выражения:", result)