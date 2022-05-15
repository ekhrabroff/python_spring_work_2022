# todo: Найти сумму элементов матрицы,
# Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423

matrix = [[1, 2, 3], [4, 5, 6]]

def msum(matrix):
    return sum([i for j in matrix for i in j])

print(f'сумма элементов матрицы {matrix} = {msum(matrix)}')

def load_matrix(filename):
    with open(filename, 'rt') as f:
        mass = f.read()
        mass = mass.split('\n')
        nums = ''.join([i + ' ' for i in mass])
        nums = nums.rstrip(' ')
        nums = [int(i) for i in nums.split(' ')]
        matrix = [[int(x) for x in i.split(' ')] for i in mass]
        result = [i for i in matrix if len(i) == len(nums) / len(matrix)]

    return result if len(result) > 0 else False

res = load_matrix('matrix.txt')
print(f'сумма элементов матрицы {res} = {msum(res)}')
