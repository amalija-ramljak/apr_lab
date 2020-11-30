import numpy as np

def box(x0, restrictions, function, epsylon=1e-6, alpha=1.3):
    x0_fits = restrictions.check_all(x0)

    # data
    n = x0.shape[0]
    xc = x0
    points = []

    xd = restrictions.get_lower()
    xg = restrictions.get_upper()
    for i in range(2*n):
        R = np.random.random((n, 1))
        xi = xd + R*(xg-xd)
        while not restrictions.check_implicit(xi):
            xi = 0.5 * (xi + xc)
        points.append(xi)
        xc = calculate_centroid(points, function)
    
    xl = calculate_best(points, function)[0]
    xh = calculate_worst(points, function)[0]
    iteration_guard = 100
    while calculate_distance(xl, xh) > epsylon or iteration_guard > 0:
        previous_xl = calculate_best(points, function)[0]
        h = calculate_worst(points, function)
        xh = h[0]
        hi = h[1]
        xh2 = calculate_second_worst(points, function)[0]
        xc = calculate_centroid(np.delete(points, hi, 0), function)
        # refleksija
        xr = (1+alpha)*xc - alpha*points[hi]
        # snappanje na eksplicitne granice
        for i in range(n):
            if xr[i, 0] < xd[i, 0]:
                xr[i, 0] = xd[i, 0]
            elif xr[i, 0] > xg[i, 0]:
                xr[i, 0] = xg[i, 0]
        # privlacenje unutar implicitnih granica
        while not restrictions.check_implicit(xr):
            xr = 0.5 * (xr + xc)
        if function(xr) > function(xh2):
            xr = 0.5 * (xr + xc)
        points[hi] = xr
        xl = calculate_best(points, function)[0]
        if function(xl) - function(previous_xl) <= epsylon:
            iteration_guard -= 1
        else:
            iteration_guard = 100
        xh = calculate_worst(points, function)[0]
    return xl

def calculate_centroid(points, function):
    xc = np.zeros_like(points[0])
    for p in points:
        xc = xc + p
    return xc / (len(points))

def calculate_best(points, function):
    xl = points[0]
    index = 0
    for i, point in enumerate(points):
        if function(point) < function(xl):
            xl = point
            index = i
    return xl, index

def calculate_worst(points, function):
    xh = points[0]
    index = 0
    for i, point in enumerate(points):
        if function(point) > function(xh):
            xh = point
            index = i
    return xh, index

def calculate_second_worst(points, function):
    h = calculate_worst(points, function)[0]
    fh = function(h)
    h2 = points[0]
    index = 0
    for i, point in enumerate(points):
        if function(point) > function(h2) and function(point) < fh:
            h2 = point
            index = i
    return h2, index

def calculate_distance(x1, x2):
    return np.linalg.norm(x1-x2)
