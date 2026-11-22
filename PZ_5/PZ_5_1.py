# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится ноль
def solve_task_1(number):
    steps = 0
    while number > 0:
        digit_sum = sum(int(digit) for digit in str(number))
        number = number - digit_sum
        steps += 1
    return steps
n = input("Введите число: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")
print('Количество действий до нуля: ', solve_task_1(n))