import psycopg

class DB:
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются
        атрибуты доступа к БД. Метод возвращает соединение.'''

    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            cls.__instance__ = object.__new__(cls)
            return cls.__instance__
        else:
            raise Exception(f"Нельзя создать более одного объекта класса {DB.__name__}")

    def __init__(self, database, user, passw):

        self.database = database
        self.user = user
        self.passw = passw

    def getconnect(self):
        conn = psycopg.connect(f"dbname={self.database} user={self.user} password={self.passw}")
        return conn

class Person(object):
    instance = None
    __slots__ = ['name', 'surname']

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Car():
    color = "Red"

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"Модель: {self.model} c ценой {self.price} "

    def __add__(self, other):
        return (int(self.price) + int(other.price))



car_one = Car("Mercedes-benz", "5000000")
car_two = Car("Aurus Senat", "50000000")
cars = car_one + car_two
print(cars)


db1 = DB('testsystem', 'testsystem', 'test12345')
conn = db1.getconnect()
print(db1.__doc__)
print('Connection:', conn)
conn.close()


try:
    db2 = DB('testsystem', 'testsystem', 'test12345')
    con1 = db2.getconnect()
except Exception as err:
    print(err)

pers = Person('Вася', 'Петров')





# class Coffee:
#     def __init__(self, milk, beans):
#         self.milk = milk
#         self.coffee = 100-milk
#         self.beans = beans
#
#     def __repr__(self):
#         return f'Milk={self.milk}% Coffee={self.coffee}% Beans={self.beans}'
#
#     @classmethod
#     def cappuccino(cls):
#         return cls(80, 'Arrabica')
#
#     @classmethod
#     def espresso_macchiato(cls):
#         return cls(30, 'Robusta')
#
#     @classmethod
#     def latte(cls):
#         return cls(95, 'Arrabica')
#
#
# print(Coffee.cappuccino())
# print(Coffee.espresso_macchiato())
# print(Coffee.latte())

