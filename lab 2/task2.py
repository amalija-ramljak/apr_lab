from hooke_jeeves import hooke_jeeves
from nelder_mead import simplex
from coordinate_axes import axes_search
from functions import *
import numpy as np

def main():
    # FUNCTION 1 / banana
    fun1_start = np.array([-1.9, 2.0])
    fun1 = Function(f1)
    # fun1_min_axes = axes_search(fun1_start, f1)
    fun1_min_simp = simplex(fun1_start, f1)
    fun1_min_hoje = hooke_jeeves(fun1_start, f1)

    # FUNCTION 2
    fun2_start = np.array([0.1, 0.3])
    fun2 = Function(f2)
    # fun2_min_axes = axes_search(fun2_start, f2)
    fun2_min_simp = simplex(fun2_start, f2)
    fun2_min_hoje = hooke_jeeves(fun2_start, f2)

    # FUNCTION 3
    fun3_start = np.array([0.0 for i in range(5)])
    fun3 = Function(f3)
    # fun3_min_axes = axes_search(fun3_start, f3)
    fun3_min_simp = simplex(fun3_start, f3)
    fun3_min_hoje = hooke_jeeves(fun3_start, f3)

    # FUNCTION 4 / jakobovic
    fun4_start = np.array([5.1, 1.1])
    fun4 = Function(f4)
    # fun4_min_axes = axes_search(fun4_start, f4)
    fun4_min_simp = simplex(fun4_start, f4)
    fun4_min_hoje = hooke_jeeves(fun4_start, f4)

    print("\n\nSolutions")
    print("\tHooke-Jeeves\t\t\tSimplex")
    print("F1\t%-30s\t%-30s" % (fun1_min_hoje, fun1_min_simp))
    print("F2\t%-30s\t%-30s" % (fun2_min_hoje, fun2_min_simp))
    print("F3\t%-30s\t%-30s" % (fun3_min_hoje, fun3_min_simp))
    print("F4\t%-30s\t%-30s" % (fun4_min_hoje, fun4_min_simp))

