# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

a = int(input("Ввведите A "))
b = int(input("Ввведите B "))

if a == 0:
    print("Коэффициент A не должен быть равен нулю ")
else:
    print(-b / a)