#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

N = [i for i in range(10)]

print("Заданный массив:",N)

for i in N:
    N[i] = N[i] + 1
print("Увеличиваем каждый эллемент на единицу",N)