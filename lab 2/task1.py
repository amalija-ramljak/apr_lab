from golden_ratio import calculate_golden
from coordinate_axes import axes_search
from hooke_jeeves import hooke_jeeves
from nelder_mead import simplex
from functions import Function
import numpy as np

def function(x):
    return np.sum((x-3)**2)

def main():
    start = 10.0
    fun = Function(function).call
    a, b = calculate_golden(fun, start, t='p')
    print("\nGolden", (a+b)/2, "\n\n")
    x = np.array([start])
    xmin = axes_search(x, fun)
    print("\nAxes", xmin)
    xmin = hooke_jeeves(x, fun)
    print("\nHooke Jeeves", xmin)
    xmin = simplex(x, fun)
    print("\nSimplex", xmin)