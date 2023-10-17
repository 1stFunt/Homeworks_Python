# Напишите функцию для транспонирования матрицы
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


original_matrix = [[1, 2, 3], [4, 5, 6],]
for row in original_matrix:
    print(row)
print()
transposed_matrix = transpose_matrix(original_matrix)
for row in transposed_matrix:
    print(row)
