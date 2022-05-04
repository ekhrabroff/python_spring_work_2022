#todo: Сформируйте таблицу переходов для задачи 12 лекция 3.

#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер

area = {'kg': (lambda x: x),
        'mg': (lambda x: x / 1000000),
        'g' : (lambda x: x / 1000),
        't' : (lambda x: x * 1000),
        'ct': (lambda x: x * 100)
}

num = int(input('Ввведите число: '))
print('кг в кг', area['kg'] (num))
print('мг в кг ', area['mg'] (num))
print('г в кг ', area['g'] (num))
print('тонны в кг ', area['t'] (num))
print('центнеры в кг ', area['ct'] (num))

