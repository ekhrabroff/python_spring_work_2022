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

mass = [1, -5, 6, 3, 101, 36]
log = {}  # словарь для сохранения вызванных функций и кол-ва вызовов функции {'имя_функции': кол-во вызовов}


def decoraror_func(func):
    def wrapper(*args):
        global log
        if func.__name__ in log.keys():  # func.__name__ - возвращает название переданной функции
            log[func.__name__] += 1  # если функция вызывалась ранее увеличиваем счетчик кол-ва вызовов в словаре
        else:
            log[func.__name__] = 1  # если функция вызвана впервые добавляем ее название и кол-во вызовов в словарь

        func(*args)

        return func(*args)

    return wrapper


def save_log(log: dict):  # функция сохранения лога в файл
    now = datetime.now()
    with open('debug.log', 'at') as f:
        for i in log.keys():
            print(f'{i}, {log[i]}, {now.strftime("%d.%m.%Y, %H:%M:%S")}')
            f.write(f'{i}, {log[i]}, {now.strftime("%d.%m.%Y, %H:%M:%S")}\n')


@decoraror_func  # декорируем render
def render(text):
    text = text.upper()
    return text


@decoraror_func  # декорируем mass_sorted
def mass_sorted(mass):
    mass = mass.sort()


@decoraror_func  # декорируем summ
def summ(*summ):
    s = 0
    for i in summ:
        s = s + int(i)
    return s


render('Hi')

print(f'Сумма равна {summ(10, 15, 18, 19, 20)}')

mass_sorted(mass)

mass_sorted(['7, -1, 10, 3'])

summ(5, 5)
summ(100, 1000, 350, -8, 60)

print(render('hello world'))
render('how are you')

save_log(log)

