

def encode_cyr_char(letter, offset):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if letter in alphabet:
        return alphabet[alphabet.index(letter)-int(offset)]
    else:
        return letter
     


str_num = 1
encode_str = ''

f = open("message.txt","r")

for i in f:
    count = 1
    while count <= len(i):
        encode_str += encode_cyr_char(i[count-1],str_num)
        count += 1
    print(encode_str)
    encode_str = ''
    str_num += 1
            
f.close



