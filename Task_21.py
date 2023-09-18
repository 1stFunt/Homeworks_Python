# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения, сложения, умножения матриц.
class Matrix:
    """
    Класс Matrix представляет матрицу и предоставляет методы для работы с ней.
    Args:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.
    Attributes:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.
        data (list): Двумерный список, представляющий данные матрицы.
    Methods:
        fill(elements): Заполняет матрицу значениями из переданного списка элементов.
        __str__(): Возвращает строковое представление матрицы.
        __eq__(other): Проверяет, равны ли две матрицы.
        __mul__(other): Выполняет умножение матрицы на другую матрицу.
        __add__(other): Выполняет сложение матрицы с другой матрицей.
    """

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def fill(self, elements):
        if len(elements) != self.rows * self.columns:
            raise ValueError(
                "Количество элементов должно соответствовать размеру матрицы.")
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = elements[i * self.columns + j]

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError(
                    "Количество столбцов в первой матрице должно совпадать с количеством строк во второй матрице.")
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Неподдерживаемый тип умножения.")

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.columns != other.columns:
                raise ValueError(
                    "Размеры матриц не совпадают, сложение невозможно.")
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Неподдерживаемый тип сложения.")


# Пример умножения и сравнения для матриц
matrix1 = Matrix(2, 3)
matrix1.fill([1, 2, 3, 4, 5, 6])
matrix2 = Matrix(3, 2)
matrix2.fill([7, 8, 9, 10, 11, 12])
print("Матрица 1:")
print(matrix1)
print("Матрица 2:")
print(matrix2)
print("Сравнение матриц:")
print(matrix1 == matrix2)
print("Умножение матриц:")
result_matrix_multiply = matrix1 * matrix2
print(result_matrix_multiply)

# Пример сложения для матриц
matrix3 = Matrix(2, 2)
matrix3.fill([1, 2, 3, 4])
matrix4 = Matrix(2, 2)
matrix4.fill([5, 6, 7, 8])
result_matrix_addition = matrix3 + matrix4
print("Сложение матриц:")
print(result_matrix_addition)