import numpy as np

from gradient import steepest_descent as sd
from newton_raphson import newton_raphson as nr
from functions import Function, f1, f1_gradient, f1_hesse, f2, f2_gradient, f2_hesse

golden = True
fun1 = Function(f1, f1_gradient, f1_hesse)
f1_x0 = np.array([[-1.9],[2.0]])

fun2 = Function(f2, f2_gradient, f2_hesse)
f2_x0 = np.array([[0.1],[0.3]])

# gradient
print("Steepest descent")
x1 = sd(f1_x0, fun1, golden=golden)
print("\tFunction 1")
print("\t\tMinimum reached", x1.T)
print("\t\tFunction called", fun1.call_count, "times.")
print("\t\tGradient calculated", fun1.gradient_count, "times.")
print("\t\tHesse matrix calculated", fun1.hesse_count, "times.")
x2 = sd(f2_x0, fun2, golden=golden)
print("\tFunction 2")
print("\t\tMinimum reached", x2.T)
print("\t\tFunction called", fun2.call_count, "times.")
print("\t\tGradient calculated", fun2.gradient_count, "times.")
print("\t\tHesse matrix calculated", fun2.hesse_count, "times.")

fun1.reset_calls()
fun2.reset_calls()
# newton-raphson
print("Newton-Raphson")
x1 = nr(f1_x0, fun1, golden=golden)
print("\tFunction 1")
print("\t\tMinimum reached", x1.T)
print("\t\tFunction called", fun1.call_count, "times.")
print("\t\tGradient calculated", fun1.gradient_count, "times.")
print("\t\tHesse matrix calculated", fun1.hesse_count, "times.")
x2 = nr(f2_x0, fun2, golden=golden)
print("\tFunction 2")
print("\t\tMinimum reached", x2.T)
print("\t\tFunction called", fun2.call_count, "times.")
print("\t\tGradient calculated", fun2.gradient_count, "times.")
print("\t\tHesse matrix calculated", fun2.hesse_count, "times.")
