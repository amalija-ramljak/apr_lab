from Matrix import Matrix

print("\n\nTask 7 - Inexistent inverse")

matrix = Matrix(data=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

try:
    print(matrix**-1)
except TypeError as e:
    print(e)