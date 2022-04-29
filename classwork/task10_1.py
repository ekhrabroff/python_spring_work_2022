#todo: Создайте объект сериализации любым методом для соседа, запишите его в файл,
# педайте его ему для считывания. Соседу необходимо десириализовать полученый объект.

import pickle

dict = {'name': ['Саша', 'Петя', 'Ваня', 'Махмуд'],
        'age': (10,15,30,45), 'Bool': True}

string = 'abcdefg'

with open('dump.pcl', "wb") as f:
       pickle.dump(dict,f)
       pickle.dump(string,f)




