# Дано целое число N (> 0). Найти сумму 1N + 2N-1 + ... + N1
N = int(input("Введите целое число:"))
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели.")
        N = input("Введите целое число:")
total_sum = 0
i = 1
while i <= N:
    power = N - i + 1
    total_sum += i ** power
    i += 1
print("Сумма:", total_sum)