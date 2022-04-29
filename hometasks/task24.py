lat = "abcdefghijklmnopqrstuvwxyz"
text = input('Введите строку: ')
s = ''
i = 0
text_nev = text
while i < len(text):
    a = text[i]
    while '0' <= a <= '9':
        s += a
        i += 1
        if i < len(text):
            a = text[i]
        else:
            break
    i += 1
    if s != '':
        text_nev = text_nev.replace(s, lat[int(s)-1])
        s = ''
print(text_nev)