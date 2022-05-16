# #todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.
#
#
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||

def transpose(matrix):
    col = len(matrix)
    row = len(matrix[0])
    
    return [[matrix[i][j] for i in range(col)] for j in range(row)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9,]]
print("Исходная матрица", matrix)
print("Транспонированная матрица", transpose(matrix))