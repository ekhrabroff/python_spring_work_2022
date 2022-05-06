#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
#написать Save Game по следующему сценарию:
#В запущенной игре по нажатию клавиши S появляется вывод:
#1. Продолжить
#2. Сохранить игру

#При выборе пункта 1. игра продолжается.
#При выборе пункта 2. пользователю предлагается ввести название для
#сохранения, после чего нужно сделать сериализацию состояния игры.
#Законсервировать все объекты которые отвечают за состоянии игры в файл
#game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.

#При старте игры пользователю должен предлагатся выбор
#1. Новая игра
#2. Восстановить игру
#При выборе 1. начинается новая игра.
#При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
#Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import random, pickle

saved_games = [] # Список сохраненных игр

obj = { 'num':random.randint(0, 100), # Случайное число
        'res' : 0,      # текущий ответ
        'attemp': 10,   # количество попыток
        'count' : 0,    # Текущая попытка
        'answers' : [], # Введенные ответы
        'save_name':0}  # Имя игры для сохранения

def save_game(object, file):
        global obj
        obj['save_name'] = input('Введите название для сохранения: ')
        with open(file,'ab') as f:
                pickle.dump(object,f)
        print('Игра сохранена. Продолжаем играть')

def load_game(object: list, file):
        global obj
        try:
                with open(file, "rb") as f:
                        while True:              # читаем pkl файл до конца
                                try:
                                        object.append(pickle.load(f)) # добавляем сохранение в список
                                except EOFError: # исключение конец файла
                                        break
        except FileNotFoundError: # исколючение - если файл не найден
                print('Сохраненные игры отсутствуют. Начинаем новую игру')
                return -1

        for i in object: # выводим на экран список всех сохраненных игр
                print(str((object.index(i) + 1)) + '.', object[object.index(i)] ['save_name'])

        num = int(input('Введите номер сохраненной игры для загрузки: '))
        if 0 <= num <= len(object):
                obj = object[num-1]
        else:
                print('Введен неверный номер сохраненной игры. Загружено последнее сохранение')
                obj = object[len(object) - 1]

        print('Загружена игра:', obj['save_name'])
        print('Использовано попыток:', obj['count'])
        print('Осталось попыток:', obj['attemp'] - obj['count'])
        answers = ''
        for i in obj['answers']:
                answers += i + ' '
        print('Ранее введенные ответы:', answers)


def game_start():
        global obj
        choice = 0
        print('Для подсказки нажмите клавишу H')
        while obj['count'] != obj['attemp']:
                obj['res'] = input('Введите число: ')

                if obj['res'].isdigit():
                        obj['answers'].append(obj['res'])
                if obj['res'] == str(obj['num']):
                        print('Поздравляю! Вы угадали с', obj['count'] + 1, 'попытки')
                        break
                elif obj['res'] == 'S' or obj['res'] == 's':
                        print('1. Продолжить')
                        print('2. Сохранить игру')
                        choice = input('Выберите действие: ')
                        if choice == '1':
                                print('Продолжаем игру')
                                continue
                        elif choice == '2':
                                save_game(obj, 'game_dump.pkl')
                                continue
                        else:
                                print('Вы ввели неверное значение. Продолжаем игру')
                                continue
                elif obj['res'] == 'H' or obj['res'] == 'h':
                        print('Загаданное число:', obj['num'])
                        continue

                else:
                        if obj['res'].isdigit():
                                obj['count'] += 1
                                if int(obj['res']) > obj['num']:
                                        print('Загаданное число меньше чем', obj['res'])
                                else:
                                        print('Загаданное число больше чем', obj['res'])
                                if obj['count'] == obj['attemp']:
                                        print('Вы израсходовали все попытки. Game over!')
                                else:
                                        print('У вас осталось', obj['attemp'] - obj['count'], 'попыток')

                        else:
                                print('Введите числовое значение или нажмите клавишу S или H')
                                continue



print("""
Поиграем в игру "отгадай число от 0 до 100"

1. Новая игра
2. Восстановить игру
""")

choice = input('Выберите действие: ')

if choice == '1':
        game_start()
elif choice == '2':
        load_game(saved_games, 'game_dump.pkl')
        game_start()
else:
        print("Введен некорректный ответ")







