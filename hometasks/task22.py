#Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
#циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


def encode_cyr_char(letter, offset):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if letter in alphabet:
        return alphabet[alphabet.index(letter)-int(offset)]
    else:
        return letter
     


str_num = 1
encode_str = ''

f = open("message.txt","r", encoding="UTF8")

for i in f:
    count = 1
    while count <= len(i):
        encode_str += encode_cyr_char(i[count-1],str_num)
        count += 1
    print(encode_str)
    #encode_str = ''
    str_num += 1
            
f.close



