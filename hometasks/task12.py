#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4

#Введите  массу тела
#>1

#Ответ: 1000 кг

x = float(input("Введите единицу массы тела:"))
s = float(input("Введите массу тела:"))

if x >= 1 and x <=5:
    match x:
        case 1:
            print(s,"кг")
        case 2:
            print(s / 1e6,"кг")
        case 3:
            print(s / 1000,"кг")
        case 4:
            print(s * 1000,"кг")
        case 5:
            print(s * 100,"кг")
else:
    print("Единица массы должна быть от 1 до 5")





