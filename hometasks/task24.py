# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

latin = ''.join([chr(i) for i in range(ord("a"), ord("a") + 26)]) # создаем алфавит от a до z

a = '8 5 12 12 15 '
b = '8 5 12 12 15 , 0 23 15 18 12 4 ! '

def num_to_letter(num_string, alphabet) -> str:
    res = num_string.split(" ")
    for i in res:
        if i.isdigit():
            if i == '0':
                res[res.index(i)] = ' '
            else:
                res[res.index(i)] = alphabet[int(i) - 1]
    res = ''.join(res)
    return res

print(num_to_letter(a, latin))
print(num_to_letter(b, latin))



