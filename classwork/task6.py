# :todo Написать функцию is_ascending(list_) проверки на монотонность?
#Функция принимает список и определяет  является ли он монотонно возрастающим
#(то есть проверяет верно ли, что каждый элемент этого списка больше предыдущего).
#В качестве результата возвращайте  YES, если массив монотонно возрастает и NO в противном случае.

#Пример:
#mass = [ 2, 5, 7]

#def is_ascending(list_):
#    ваша реализация


#result = is_ascending(mass)
#print(result)
#YES

mass = [2, 15, 17, 18, 230, 231, 232]
mass_1 = [2, 15, 16, 14, 205, 206]

def is_ascending(list_):
    count = 0
    result = ""
    while count != (len(list_)-1):
        if list_[count] < list_[count+1]:
            result = "YES"
        else:
            result = "NO"
            break
        count = count +1
    return result

print("Задан массив", mass)
result = is_ascending(mass)
print("Массив является монотонно возрастающим?")
print(result)
print("Задан массив", mass_1)
result = is_ascending(mass_1)
print("Массив является монотонно возрастающим?")
print(result)



