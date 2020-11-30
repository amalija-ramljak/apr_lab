import numpy as np

from mixed_tf import transform
from functions import Function, f1, f1_gradient, f1_hesse, f2, f2_gradient, f2_hesse
from Restrictions import Restrictions

fun1 = Function(f1, f1_gradient, f1_hesse)
f1_x0 = np.array([[-1.9],[2.0]])

fun2 = Function(f2, f2_gradient, f2_hesse)
f2_x0 = np.array([[5],[5]])

implicit_ineq = [
    lambda x: x[1,0] - x[0,0],
    lambda x: 2 - x[0,0]
]

rest = Restrictions(implicit_ineq=implicit_ineq)

x1 = transform(f1_x0, fun1, rest)
print("Function 1")
print("\tMinimum", x1.T)
x2 = transform(f2_x0, fun2, rest)
print("Function 2")
print("\tMinimum", x2.T)