# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе

#тип сортировки: 1

#Затем сообщение для ввода
#Ввидите критерии поиска: 16

#Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

print("Введите тип сортировки")
print("1. По возрасту")
print("2. По первой букве")
print("3. По группе ")

sort_type = int(input())
value = input("Введите критерии поиска:")

element = 0
for i in users:
    dic = users[element]
    element = element + 1
    first_letter = str(dic.get('login'))
    match sort_type:
        case 1:
            if int(dic['age']) > int(value):
                print("Пользователь",dic['login'],"возраст",dic['age'],"Группа",dic['group'] )
            else:
                print("Пользователи старше",value,"лет отсуствуют в базе")
                break
        case 2:
            if value == first_letter[0]:
                print("Пользователь", dic['login'], "возраст", dic['age'], "Группа", dic['group'])
            else:
                print("Пользователи начинающиеся на букву", value, "отсуствуют в базе")
                break















