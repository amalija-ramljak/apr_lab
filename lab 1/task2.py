from Matrix import Matrix
from constants import *

print("\n\nTask 2 - LU or LUP?")

b = ~Matrix(data=[[12, 12, 1]])
A_data = [
    [3, 9, 6],
    [4, 12, 12],
    [1, -1, 1]
]
A = Matrix(data=A_data)
try:
    LU = A.copy().LU_decomposition()
    y = LU.forward_substitution(b.copy())
    x = LU.backward_substitution(y)
    print("LU solution")
    print(x)
except ValueError as e:
    print(e)

try:
    LU, P = A.LUP_decomposition()
    b.permutation(P)
    y = LU.forward_substitution(b)
    x = LU.backward_substitution(y)
    print("\nLUP solution")
    print(x)
except ValueError as e:
    print(e)
