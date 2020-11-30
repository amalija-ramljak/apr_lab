import numpy as np

from box import box
from functions import Function, f1, f1_gradient, f1_hesse, f2, f2_gradient, f2_hesse
from Restrictions import Restrictions

fun1 = Function(f1, f1_gradient, f1_hesse)
f1_x0 = np.array([[-1.9],[2.0]])

fun2 = Function(f2, f2_gradient, f2_hesse)
f2_x0 = np.array([[0.1],[0.3]])

implicit_ineq = [
    lambda x: x[1,0] - x[0,0],
    lambda x: 2 - x[0,0]
]

rest = Restrictions(lower_border=np.array([[-100],[-100]]), upper_border=np.array([[100],[100]]), implicit_ineq=implicit_ineq)

x1 = box(f1_x0, rest, fun1)
print("Function 1")
print("\tMinimum", x1.T)
x2 = box(f2_x0, rest, fun2)
print("Function 2")
print("\tMinimum", x2.T)