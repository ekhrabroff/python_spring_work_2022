# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

latin = "abcdefghijklmnopqrstuvwxyz"

s = input("Введите числа для замены на буквы: ")
obj = ''
count = 0

for i in s:
    if i.isdigit():
        if i == '0':
            s = s.replace(i, "")
        obj += ''.join(i)
        continue
    elif obj != '':
        print(obj, '-', latin[int(obj) - 1]) # раскоменти для вывода на экран
        s = s.replace(obj, latin[int(obj) - 1]) # почему выдает неккоректный результат на числе 15, если оно оно идет третим в строке?
    elif i.isdigit() == False:
        obj = ''
        continue
    obj = ''
print(s)



