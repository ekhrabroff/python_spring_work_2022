# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

latin = "abcdefghijklmnopqrstuvwxyz"

s = input("Введите числа для замены на буквы: ")
res = ''
count = 0

for i in s:
    if i.isdigit():
        if i == '0':
            s = s.replace(i, "")
        res += i
        continue
    elif res != '':
        s = s.replace(res, latin[int(res) - 1]) # почему выдает неккоректный результат на числе 15, если оно оно идет третим в строке?
    elif i.isdigit() == False:
        res = ''
        continue
    res = ''
print(s)



