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


obj = { 'num':random.randint(0, 100),
        'res' : 0,
        'attemp': 10,
        'count' : 0
        'dump_input':0}

def save_game(obj, file):
        with open(file,'ab') as f:
                pickle.dump(obj,f)

def game_start():
        global obj
        choice = 0
        while obj['count'] != obj['attemp']:
                obj['res'] = input('Введите число: ')
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

                                print('Игра сохранена. Продолжаем играть')
                                continue
                        else:
                                print('Вы ввели неверное значение. Продолжаем игру')
                                continue

                else:
                        if obj['res'].isdigit():
                                obj['count'] += 1
                                if obj['res'] > str(obj['num']):
                                        print('Загаданное число меньше чем', obj['res'])
                                else:
                                        print('Загаданное число больше чем', obj['res'])
                                print('У вас осталось', obj['attemp'] - obj['count'], 'попыток')
                        else:
                                print('Введите числовое значение или нажмите клавишу S')
                                continue

with open('game_dump.pkl', 'r+b') as f:
        obj1 = pickle.load(f)
print(obj1)
print(obj['num'])
game_start()






