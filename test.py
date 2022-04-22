# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

a = int(input())
b = int(input())
c = int(input())

a1 = a
b1 = b
c1 = c

b = a1
c = b1
a = c1

print(a,b,c)