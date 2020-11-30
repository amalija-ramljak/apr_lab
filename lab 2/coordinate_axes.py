from copy import deepcopy
import numpy as np
from golden_ratio import calculate_golden

def axes_search(x0, function, epsylon=1e-6):
    n = len(x0)
    x = deepcopy(x0)
    while True:
        xs = deepcopy(x)
        for i in range(n):
            e_i = np.zeros_like(x)
            e_i[i] = 1.0
            fun = lambda x: function(xs + x * e_i)
            print("\n\nNew lambda")
            a,b = calculate_golden(fun, 0, 'p')
            lamb = (a+b)/2
            x += lamb * e_i
        if np.linalg.norm(x-xs) <= epsylon:
            return x