import numpy as np
from functions import Function, f3, f3_gradient, f3_hesse
from gradient import steepest_descent as sd

f = Function(f3, f3_gradient, f3_hesse)
x0 = np.array([[0],[0]])

xmin_nogolden = sd(x0, f)
print("Without golden optimisation:\t", xmin_nogolden)

xmin_golden = sd(x0, f, golden=True)
print("With golden optimisation:\t", xmin_golden)