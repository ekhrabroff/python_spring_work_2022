#todo: Для каждого значения из списка mass получите
# список проверок(True или False) вхождений значений в диапазон от 1 до 100
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]

obj = list(map(lambda x: x <= 100, mass))
print(obj)



#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений

list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]

obj = list(filter(lambda x: x % 2 != 0, list_))
print(obj)