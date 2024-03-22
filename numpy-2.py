import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

result = np.dot(matrix_a, matrix_b)
print("np.dot(matrix_a, matrix_b): \n", result)

result = matrix_a.dot(matrix_b)
print("matrix_a.dot(matrix_b): \n", result)