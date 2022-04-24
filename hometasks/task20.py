#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла import_this.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

#выходные данные
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.

f = open("../../hometasks/import_this.txt", "w+")
f.write("Beautiful is better than ugly.\n")
f.write("Explicit is better than implicit.\n")
f.write("Simple is better than complex.\n")
f.write("Complex is better than complicated.\n")
f.seek(0)

lines = f.readlines()
reversed_lines = lines[::-1]

for i in reversed_lines:
   print(i)

f.close()