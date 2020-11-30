import numpy as np
from nelder_mead import simplex

def transform(x0, function, restrictions, t=1, epsylon=1e-6):
    x = x0
    if not restrictions.check_inequalities(x):
        x = find_inner_point(function, restrictions.get_inequalities())
    while True:
        print("Printing t", t)
        r = 1/t
        if not restrictions.check_inequalities(x):
            print("Cannot calc log here!")
            return np.inf
        u_xr = lambda x: function(x) - r*np.sum([np.log(ineq(x)) for ineq in restrictions.get_inequalities()]) + t*np.sum([eq(x)**2 for eq in restrictions.get_equalities()])
        previous_x = x
        x = simplex(x, u_xr)
        if np.linalg.norm(previous_x - x) <= epsylon:
            break
        t *= 10
    return x

def find_inner_point(function, inequalities, epsylon=1e-6):
    # if x0 does not fit restrictions
    g = lambda x: -np.sum([ineq(x) for ineq in inequalities if ineq(x) < 0])
    return simplex(np.array([[0],[0]]), g)

