import numpy as np

from mixed_tf import transform
from functions import Function, f4, f4_gradient, f4_hesse
from Restrictions import Restrictions

fun = Function(f4, f4_gradient, f4_hesse)
x0 = np.array([[0],[0]])

implicit_ineq = [
    lambda x: 3 - x[0,0] - x[1,0],
    lambda x: 3 + 1.5 * x[0,0] - x[1,0]
]

implicit_eq = [
    lambda x: x[1,0] - 1
]

rest = Restrictions(implicit_ineq=implicit_ineq, implicit_eq=implicit_eq)

x = transform(x0, fun, rest)
print("Function 4")
print("\tMinimum", x.T)