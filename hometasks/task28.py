# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта

from datetime import datetime

mass = [1, -5, 6, 3, 101, 36, 37, 38]
log = {}

def decoraror_func(func):
    def wrapper(*args):
        #count = 0
        global log
        if func.__name__ in log.keys():

            log[func.__name__] += 1
        else:
            log[func.__name__] = 1
        func(*args)
        with open('debug.log','wt') as f:
            for i in log.keys():
                f.write(f'{i} {log[i]} {datetime.today()}\n')
    return wrapper

@decoraror_func

def mass_sorted(mass):
    mass = mass.sort()

mass_sorted(mass)

def render(text):
    text = text.upper()
    return text

wd = decoraror_func(render)
wd('hi')

mass_sorted(mass)

wd('privet')
wd('ooops')
wd('boroda')
mass_sorted(mass)
wd('Once')

wd1 = decoraror_func(print)
wd1(wd, render('Wow'), 'Hello')
mass_sorted([14,15,-1])
wd1('Text1', wd, wd1, mass_sorted(mass))

