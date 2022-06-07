#  TODO: реализовать протокол получения файла: GET file.jpg
#

# https://docs.python.org/3/library/socket.html#module-socket
#https://pythonist.ru/rabota-s-setevymi-soketami-na-python/
import socket
# Дописать протокол передачи файла. Сперва разбираем
HOST = ''                 # Хост
PORT = 50008              # Порт сервера
# Создаем сокет


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # связываем сокет с хостом , функции bind передаем хост и порт
    s.bind((HOST, PORT))
    # запускае режим прослушивания , передаваемый параметр определяет размер очереди.
    s.listen(1)
    # принимаем подключение с помощью метода accept, который возращает кортеж с двумя элементами.
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(512000)
            print(data)
            if not data: break
            query = data.decode().split(' ') # сплитим запрос клиента в список чтобы извлечь имя файла
            if 'GET' in query:
            # если запрос содержит слово GET пытаемся открыть запрашиваемый файл
                try:
                    with open(query[1], 'rb') as f:
                        data = f.read()
                    conn.sendall(data) # если файл найден возвращаем его клиенту
                except FileNotFoundError:
                    print(f'Файл {query[1]} не найден')
                    conn.sendall(b'FileNotFoundError') # если файл не найден возвращаем клиенту ошибку
            else:
                conn.sendall(data) # если запрос не содержит GET возвращаем клиенту запрос
