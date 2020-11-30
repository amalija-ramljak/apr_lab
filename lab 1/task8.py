from Matrix import Matrix

print("\n\nTasks 8 and 9 - inverse and determinant")

matrix = Matrix(data=[
    [4, -5, -2],
    [5, -6, -2],
    [-8, 9, 3]
])

try:
    print("Determinant:")
    print(matrix.copy().determinant_LUP())
    print("\nInverse:")
    print(matrix**-1)
except TypeError as e:
    print(e)