# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a = int(input())
b = int(input())
c = int(input())
print("Длина отрезка AC",abs(c-a))
print("Длина отрезка BC",abs(c-b))
print("Сумма отрезков AC и BC",abs(c-a)+abs(c-b))