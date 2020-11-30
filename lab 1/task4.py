from Matrix import Matrix

print("\n\nTask 4 - LU vs LUP")
data = [
    [0.000001, 3000000, 2000000],
    [1000000, 2000000, 3000000],
    [2000000, 1000000, 2000000]
]
b_data = [[12000000.000001, 14000000, 10000000]]

matrix = Matrix(data=data)
b = ~Matrix(data=b_data)

try:
    LU = matrix.copy().LU_decomposition()
    y = LU.forward_substitution(b.copy())
    x = LU.backward_substitution(y.copy())
    print("LU solution")
    print(x)
except ValueError as e:
    print(e)


try:
    LU, P = matrix.copy().LUP_decomposition()
    b.permutation(P)
    y = LU.forward_substitution(b)
    x = LU.backward_substitution(y)
    print("\nLUP solution")
    print(x)
except ValueError as e:
    print(e)
