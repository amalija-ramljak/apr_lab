from copy import deepcopy

def hooke_jeeves(x0, function, dx=1, epsylon=1e-6):
    xp, xb = deepcopy(x0), deepcopy(x0)
    while dx > epsylon:
        xn = explore(xp, dx, function)
        if function(xn) < function(xb):
            xp = 2 * xn - xb
            xb = xn
        else:
            dx /= 2
            xp = xb
    return xb

def explore(xp, dx, function):
    x = deepcopy(xp)
    n = len(x)
    for i in range(n):
        P = function(x)
        x[i] += dx
        N = function(x)
        if N > P:
            x[i] -= 2*dx
            N = function(x)
            if N > P:
                x[i] += dx
    return x
