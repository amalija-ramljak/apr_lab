from Matrix import Matrix

print("\n\nTask 5 - LUP on a system. Correct solution?")

matrix = Matrix(data=[
    [0, 1, 2],
    [2, 0, 3],
    [3, 5, 1]
])
b = Matrix(data=[[6], [9], [3]])

LU, P = matrix.LUP_decomposition()
b.permutation(P)
y = LU.forward_substitution(b)
x = LU.backward_substitution(y)

print(x)
