from Matrix import Matrix


print("\n\nTask 6 - Possible issue for implementation")

matrix = Matrix(data=[
    [4000000000, 1000000000, 3000000000],
    [4, 2, 7],
    [0.0000000003, 0.0000000005, 0.0000000002]
])
b = Matrix(data=[[9000000000], [15], [0.0000000015]])

LU = matrix.copy().LU_decomposition()
y = LU.forward_substitution(b.copy())
x = LU.backward_substitution(y)
print(x)

LU, P = matrix.LUP_decomposition()
b.permutation(P)
y = LU.forward_substitution(b)
x = LU.backward_substitution(y)
print(x)