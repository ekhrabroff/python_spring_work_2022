#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

#Input             	            Output
#apple	                        aple
#25.04.2022 Good morning !!	    godmrni

s = input('Введите строку: ')
out = ''

s = s.lower()

for i in s:
    if i.isalpha():
        if s.count(i) < 2:
            out += ''.join(i)
        else:
            if i in out:
                continue
            else:
                out += ''.join(i)
    else:
        continue
            
            
print(out)

             
       
            
        

