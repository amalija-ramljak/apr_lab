import numpy as np
from golden_ratio import calculate_golden

def newton_raphson(x0, function, golden=False, epsylon=1e-6):
    x = x0
    iteration_guard = 100
    while True:
        gradient = function.get_gradient(x)
        hesse = function.get_hesse(x)
        if np.linalg.norm(gradient) <= epsylon or iteration_guard == 0:
            break
        previous_x = x
        if golden:
            gradient = gradient / np.linalg.norm(gradient)
            # H*dx = dF odnosno dx = H^-1 * dF
            dx = np.linalg.solve(hesse, gradient)
            fun = lambda t: function(x + t * dx)
            lamb_interval = calculate_golden(fun, 0, epsylon=epsylon)
            lamb = sum(lamb_interval) / 2
            x = x + lamb * dx
        else:
            x = x - np.linalg.solve(hesse, gradient)
        if function(previous_x) - function(x) < epsylon:
            iteration_guard -= 1
        else:
            iteration_guard == 100
    return x
