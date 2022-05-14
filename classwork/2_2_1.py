#todo: Реализуйте функцию которая возвращает копию списка
def identity(nums):
    return [i for i in nums]

print('Identity\n', identity([1, 2, 3, 4, 5]))
print(identity([]))
# Пример вызова:
# >>> identity([1, 2, 3, 4, 5])
# [1, 2, 3, 4, 5]
# >>> identity([])
# []

#todo: Реализуйте функцию которая возвращает степень числа каждого элемента
def power_(nums, pow):
    return [i ** pow for i in nums]

print('Power\n',power_([1, 2, 3, 4, 5],2))
print(power_([1, 2, 3, 4, 5],3))

# Пример вызова:
# >> > power_([1, 2, 3, 4, 5],2)
# [2, 4, 6, 8, 10]
# >> > power_([1, 2, 3, 4, 5],3)
# [0, 3, 6, 9, 12, 15]



#todo: Реализуйте функцию которая возвращает только четные значения
def evens(nums):
    return [i for i in nums if i % 2 == 0]

print('Evens\n', evens([1, 2, 3, 4, 5]))
print(evens([1, 3, 5]))


# Пример вызова:
# >>> evens([1, 2, 3, 4, 5])
# [2, 4]
# >>> evens([1, 3, 5])
# []
# >>> evens([-2, -4, -7])
# [-2, -4]


#todo: Верните список с размерностью слов в том случае если они не исключение
# параметр exception принимает слово которое не нужно подсчитывать
def words_not_the(sentence, exception):
    return [len(i) for i in sentence.split(' ') if i != exception]

print('words_not_the')

print(words_not_the('the quick brown fox jumps over the lazy dog', 'the' ))

# Пример вызова:
# >>> words_not_the('the quick brown fox jumps over the lazy dog', 'the' )
# [5, 5, 3, 5, 4, 4, 3]


#todo: Верните список гласных букв
def vowels(word):
    return [i for i in word if i in 'aeuioy']

print('Верните список гласных букв')
print(vowels('mathematics'))

# >>> vowels('mathematics')
# ['a', 'e', 'a', 'i']



#todo: Задан массив [ 'one', 'two', 'three' ] с помощью спискового генератора преобразовать в словарь
# вида { 1:'one', 2:'two', 3:'three' }

mass = [ 'one', 'two', 'three' ]
dic = {key + 1:val for (key,val) in enumerate(mass)}
print(dic)