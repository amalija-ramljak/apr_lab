from Matrix import Matrix
from constants import *
from math import pi, e

print("Task 1 - matrix equality and epsylon")

data = [[0.123, 0.111, pi], [1.28, 5.0, 2/3]]
matrix = Matrix(data=data)
double_number = e

print("\nFirst step - comparison with itself:")
print("Matrix is equal to self?", matrix == matrix)

print("\nSecond step - matrix divided then multiplied by the same number:")
matrix_2 = matrix.copy() * (1/double_number) * double_number
print("New matrix:\n")
print(matrix_2)
print("Old matrix:\n")
print(matrix)
print("Are they the same?", matrix == matrix_2)
print("Epsylon for comparison is equal to", EPSYLON)
