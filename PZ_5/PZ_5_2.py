# Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг:
# значение A переходит в C, значение C — в B, значение B — в A (A, B, C —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить левый циклический сдвиг для двух данных
# наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def ShiftLeft3(A, B, C):
    new_A = B
    new_B = C
    new_C = A
    return new_A, new_B, new_C

print("___Набор 1___")
a1 = input("Введите A1: ")
b1 = input("Введите B1: ")
c1 = input("Введите C1: ")

while type(a1) != float or type(b1) != float or type(c1) != float:
    try:
        a1 = float(a1)
        b1 = float(b1)
        c1 = float(c1)
    except ValueError:
        print("Неправильно ввели!")
        a1 = input("Введите A1: ")
        b1 = input("Введите B1: ")
        c1 = input("Введите C1: ")

a1, b1, c1 = ShiftLeft3(a1, b1, c1)
print("Результат 1: ", a1, b1, c1)


print("___Набор 2___")
a2 = input("Введите A2: ")
b2 = input("Введите B2: ")
c2 = input("Введите C2: ")

while type(a2) != float or type(b2) != float or type(c2) != float:
    try:
        a2 = float(a2)
        b2 = float(b2)
        c2 = float(c2)
    except ValueError:
        print("Неправильно ввели!")
        a2 = input("Введите A2: ")
        b2 = input("Введите B2: ")
        c2 = input("Введите C2: ")

a2, b2, c2 = ShiftLeft3(a2, b2, c2)
print("Результат 2: ", a2, b2, c2)
