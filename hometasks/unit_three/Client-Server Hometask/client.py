# Echo client program
import socket
import subprocess

HOST = '127.0.0.1'    # The remote host
PORT = 50008              # The same port as used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Для получения файла введите запрос "GET имя_файла"')
    query = input('Введите запрос: ').encode()
    s.sendall(query)
    data = s.recv(512000)
print('Received', len(data),'bytes')

if data == b'FileNotFoundError':
    print('Запрашиваемый файл не найден на сервере')

elif data == query:
    print('Некорректный запрос к серверу')
    print('Ответ сервера:', data)

else:
    filename = input('Введите имя файла для сохранения: ')
    with open(filename, 'wb') as f:
        f.write(data)
    code = subprocess.call(('open', filename))
    # вызываем системную функцию которая откроет файл программой по умолчанию
    if code == 0:
        print("Success!")
    else:
        print("Error!", code)

