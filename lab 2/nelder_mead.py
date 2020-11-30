import numpy as np
from copy import deepcopy

def simplex(x0, function, offset=1, alpha=1.0, beta=0.5, gamma=2, delta=0.5, epyslon=1e-6):
    x = deepcopy(x0)
    dim = len(x0)
    simplex_vertices = [x]
    for i in range(dim):
        ei = np.zeros_like(x0)
        ei[i] = offset
        simplex_vertices.append(x+ei)
    simplex_vertices.sort(key=lambda v: function(v))
    for i in range(10000):
        if np.linalg.norm(simplex_vertices[0] - simplex_vertices[-1]) < epyslon:
            break
        xh, xl = simplex_vertices[dim], simplex_vertices[0]
        fl, fh = function(xl), function(xh)
        xc = np.zeros_like(x0)
        for v in simplex_vertices:
            if (v != xh).all():
                xc = xc + v
        xc = xc / (dim+1)
        xr = reflect(xh, xc, alpha)
        fr = function(xr)
        if fr < fl:
            xe = expand(xr, xc, gamma)
            fe = function(xe)
            simplex_vertices[-1] = xe if fe < fl else xr
        else:
            condition = True
            for v in simplex_vertices:
                if (v == xh).all():
                    continue
                condition = condition and (fr > function(v))
            if condition:
                if fr < fh:
                    simplex_vertices[-1] = xr
                    fh = fr
                xk = contract(simplex_vertices[-1], xc, beta)
                fk = function(xk)
                if fk < fh:
                    simplex_vertices[-1] = xk
                else:
                    simplex_vertices = shrink(xl, simplex_vertices, delta)
            else:
                simplex_vertices[-1] = xr
        simplex_vertices.sort(key=lambda v: function(v))
    # print(i)
    return simplex_vertices[0]

def reflect(xh, xc, alpha):
    return xc + alpha * (xc - xh)

def expand(xr, xc, gamma):
    return xc + gamma * (xr - xc)

def contract(x, xc, beta):
    return xc + beta * (x - xc)

def shrink(xl, vertices, delta):
    return [xl + delta * (x - xl) for x in vertices]
