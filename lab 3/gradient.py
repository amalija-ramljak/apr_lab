import numpy as np
from golden_ratio import calculate_golden

def steepest_descent(x0, function, golden=False, epsylon=1e-6):
    x = x0
    iteration_guard = 100
    while True:
        v = - function.get_gradient(x)
        if np.linalg.norm(v) <= epsylon or iteration_guard == 0:
            break
        previous_x = x
        if golden:
            v = v / np.linalg.norm(v)
            fun = lambda t: function(x + t * v)
            lamb_interval = calculate_golden(fun, 0, epsylon=epsylon)
            lamb = sum(lamb_interval) / 2
            x = x + lamb * v
        else:
            x = x + v
        if function(previous_x) - function(x) < epsylon:
            iteration_guard -= 1
        else:
            iteration_guard = 100
    return x
