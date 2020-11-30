from Matrix import Matrix

print("\n\nTask 10 - Determinant")

matrix = Matrix(data=[
    [3, 9, 6],
    [4, 12, 12],
    [1, -1, 1]
])

det = matrix.determinant_LUP()
print(det)