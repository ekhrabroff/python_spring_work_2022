# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

a = int(input())
b = int(input())
c = int(input())

buf = b
b = a
a = c
c = buf
print(a,b,c)