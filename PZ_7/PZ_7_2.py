# Дана строка, состоящая из русских слов, набранных заглавными буквами
# и разделённых пробелами (одним или несколькими). Преобразовать каждое
# слово, заменив в нём все предыдущие вхождения его последней буквы
# на символ «.». Количество пробелов между словами не изменять.

S = input('Введите строку: ')
New_String = ''
i = 0
n = len(S)

while i < n:
    if S[i] == ' ':
        New_String = New_String + ' '
        i += 1
    else:
        j = i
        while j < n and S[j] != ' ':
            j += 1
        Slovo = S[i:j]

        last = Slovo[len(Slovo) - 1]
        New_Slovo = ''
        for t in range(len(Slovo)):
            if Slovo[t] == last and t != len(Slovo) - 1:
                New_Slovo = New_Slovo + '.'
            else:
                New_Slovo = New_Slovo + Slovo[t]
        New_String = New_String + New_Slovo
        i = j
print('Исходная строка:  ', S)
print('Преобразованная:  ', New_String)
