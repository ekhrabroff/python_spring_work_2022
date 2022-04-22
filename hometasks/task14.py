# Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2,2,2,2,2,2,]

#Для числа 2 индексы двух ближайших чисел: 6 и 9

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9

mass = [1,2,17,54,30,89,2,1,6,2,3]
result_index = []
index_count = 0

print("Задан массив",mass)
value = int(input("Введите число для поиска 2-х ближайних чисел в массиве: "))

for i in mass:
    index_count = index_count + 1
    if value == i:
        result_index.append(index_count-1)

print("Количество вхождений в массив", mass.count(value))

if (mass.count(value) == 1) or (mass.count(value) == 0):
    print("В массиве отсутствуют 2 искомых ближайших числа")
else:
    if len(result_index) > 2:
        print("Индексы 2-х ближайших чисел", result_index[1],"и",result_index[2])
    else:
        print("Индексы 2-х ближайших чисел", result_index[0],"и",result_index[1])