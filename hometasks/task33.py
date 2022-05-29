# #todo: Написать авторизацию пользователя в систему.
# Приложение в начале должно предлагать меню
# 1. Вход
# 2. Регистрация
#
#
# 1. При выборе пункта "Вход" пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
# При вводе данных авторизации, система проверяет есть ли данный
# пользователь в БД (логин) если нет то предлагает зарегистрироваться.
# Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
# приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
# выбора билетов для тестирования(пока заглушка).
#
# 2. При выборе "Регистрация" пользователю необходимо ввести новый
# логин, пароль, фио, почту, телефон, группу. После система заводит
# запись в БД если пользователя под данным логином нет. Если такой пользователь
# уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
# в виде хеша + соль.
#
# По хешированию прочитать статью
# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
# для хеширования пароля воспользоваться библиотекой bcrypt

import psycopg
import bcrypt
import datetime


def is_user_exist(login):
    "Проверяет есть ли пользователь в базе"
    with psycopg.connect('dbname=testsystem user=testsystem password=test12345') as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT login FROM public.user WHERE login LIKE '{login}'")
            return False if cur.fetchone() == None else True

def auth():
    login = input('Введите логин: ')
    passw = input('Введите пароль: ')
    if is_user_exist(login):
        with psycopg.connect('dbname=testsystem user=testsystem password=test12345') as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT login, password FROM public.user WHERE login LIKE '{login}'")
                hashed_pass = cur.fetchone()
                if bcrypt.checkpw(passw.encode(), hashed_pass[1].encode()):
                    cur.execute(f"SELECT name, surname FROM public.profile WHERE id_user = (SELECT id_user FROM public.user WHERE login LIKE '{login}')")
                    data = cur.fetchone()
                    if data != None:
                        print(f'Добро пожаловать {data[0]} {data[1]}!')
                    else:
                        print(f'Профиль пользователя {login} не найден')
                        return False
                else:
                    print('Введен неверный пароль')
                    return auth()
                return True
    else:
        print('Пользователь не найден')
        return False



def registration():
    login = input('Введите логин: ')

    if is_user_exist(login) == False or login != '':

        passw = input('Введите пароль: ')
        passw = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronym = input('Введите отчество: ')
        dt_birth = input('Введите дату рождения (дд.мм.гггг): ')
        dt_birth = [int(i) for i in dt_birth.split('.')]
        dt_birth = datetime.date(dt_birth[2], dt_birth[1], dt_birth[0])
        age = datetime.datetime.today().year - dt_birth.year
        email = input('Введите эл.почту: ')
        tel = input('Введите телефон: ')
        group = input('Введите группу: ')

    else:
        print('Логин пустой или такой пользователь уже существует. Введите другой логин')
        return registration()

    try:
        with psycopg.connect('dbname=testsystem user=testsystem password=test12345') as conn:
            with conn.cursor() as cur:
                dt_create = datetime.datetime.today()
                "Создаем пользователя в таблице user"
                cur.execute(f"""
                       INSERT INTO public.user (login, password, dt_create) 
                       VALUES ('{login}', '{passw.decode()}', '{dt_create.strftime("%Y-%m-%d")}')""")
                # conn.commit()

                cur.execute(f"SELECT id_group FROM public.group WHERE name LIKE '{group}'")
                if cur.fetchone() == None:
                    cur.execute(f"INSERT INTO public.group (name) VALUES ('{group}')")
                    # conn.commit()

                cur.execute(f"""SELECT id_student FROM student 
                       WHERE id_user = (SELECT id_user FROM public.user WHERE login LIKE '{login}') """)
                if cur.fetchone() == None:
                    cur.execute(f"""INSERT INTO public.student (id_group, name, surname, age, tel, id_user)
                           VALUES
                           ((SELECT id_group FROM public.group WHERE name LIKE '{group}'), '{name}', '{surname}', '{age}', '{tel}',
                           (SELECT id_user FROM public.user WHERE login LIKE '{login}'))""")
                # conn.commit()

                cur.execute(f"""
                       INSERT INTO profile (id_user, id_student, name, surname, patronymic, dt_birth, tel, email, id_group)
                       VALUES 
                       ((SELECT id_user FROM public.user WHERE login LIKE '{login}'), 
                       (SELECT id_student FROM student WHERE id_user = (SELECT id_user FROM public.user WHERE login LIKE '{login}')), 
                       '{name}', '{surname}', '{patronym}', '{dt_birth.strftime("%Y-%m-%d")}', '{tel}', '{email}',
                       (SELECT id_group FROM public.group WHERE name LIKE '{group}'))""")

    # except psycopg.errors.UniqueViolation as err:
    #     print('Такой номер телефона уже есть в базе')
    #     print(err)
    #     tel = input('Введите другой телефон: ')

    except psycopg.Error as err:
        print('Ошибка регистрации нового пользователя. Тип ошибки:', type(err))
        print(err)
        main()

    else:
        print(f"Пользователь {login} успешно зарегистрирован")
        return True

def main():
    print('1. Вход \n2. Регистрация')
    inp = input('Выберите действие: ')
    if inp == '1':
        if auth():
            test = input('Выберите билет для тестирования:')
            return
        else:
            print('Вы хотите зарегистрироваться? \n 1. Да \n 2. Нет')
            choice = input('Выберите действие: ')
            if choice == '1':
                print('Регистрация нового пользователя \n')
                if registration():
                    return main()
            elif choice == '2':
                print('До новых встреч!')
                return
            else:
                print('Вы выбрали неверное действие')
                return main()
    elif inp == '2':
        print('Регистрация нового пользователя \n')
        if registration():
            return main()
    else:
        print('Вы выбрали неверное действие')
        return main()

main()


