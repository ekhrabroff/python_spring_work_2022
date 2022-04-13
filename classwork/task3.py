# todo: Задана поизвольная строка. Необходимо разбить ее на две части.
# Задачу решить с помощью срезов.
#
# Пример:
# str = "Hello world!"
# Ответ: Первая часть  "Hello"
# 		Вторая часть "world!"

s = input("Введите строку ")
a = len(s)
print (a)

if (a % 2 == 0):
    part_1 = s[:int(a/2)]
    part_2 = s[int(a/2):]
    print (a % 2)

else:
    s = s + "X"
    a = len(s)
    part_1 = s[:int(a / 2)]
    part_2 = s[int(a / 2):]
    print (a % 2)

print("Первая часть",part_1)
print("Вторая часть",part_2)