from Matrix import Matrix

print("\n\nTask 3 - LU/LUP - solvable system?")

matrix = Matrix(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix(data=[[1], [2], [3]])

try:
    LU = matrix.copy().LU_decomposition()
    y = LU.forward_substitution(b.copy())
    x = LU.backward_substitution(y)
    print("LU solution:")
    print(x)
except ValueError as e:
    print(e)

try:
    LU, P = matrix.copy().LUP_decomposition()
    b.permutation(P)
    y = LU.forward_substitution(b)
    x = LU.backward_substitution(y)
    print("LUP solution:")
    print(x)
except ValueError as e:
    print(e)