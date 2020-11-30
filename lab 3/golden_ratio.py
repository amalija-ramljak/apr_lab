from copy import deepcopy

def golden_ratio(a, b, function, epsylon=1e-6):
    k = (5**0.5 - 1) / 2
    c = b - k * (b - a)  # pomaknemo se ulijevo od desne granice
    d = a + k * (b - a)  # jednako se pomaknemo udesno od lijeve
    fc = function(c)
    fd = function(d)
    i = 0
    while (b - a) > epsylon:
        i += 1
        # print("\nStep", i)
        # print("\tPoint a -", "{:.5f}".format(a), "\t\tFunction value - {:.6f}".format(function(a)))
        # print("\tPoint b -", "{:.5f}".format(b), "\t\tFunction value - {:.6f}".format(function(b)))
        # print("\tPoint c -", "{:.5f}".format(c), "\t\tFunction value - {:.6f}".format(function(c)))
        # print("\tPoint d -", "{:.5f}".format(d), "\t\tFunction value - {:.6f}".format(function(d)))
        if fc < fd:
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = function(c)
        else:
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = function(d)
    return a, b

def unimodal_interval(offset, start, function):
    left, right = start - offset, start + offset
    m = start
    step = 1
    fm = function(start)
    fl = function(left)
    fr = function(right)
    if fm < fr and fm < fl:
        return left, right
    elif fm > fr:
        while fm > fr:
            left = m
            fl = fm
            m = right
            fm = fr
            right = m + offset * step
            step *= 2
            fr = function(right)
    else:
        while fm > fl:
            right = m
            fr = fm
            m = left
            fm = fl
            left = m - offset * step
            step *= 2
            fl = function(left)
    return left, right

def calculate_golden(function, point, t='p', offset=1, epsylon=1e-6):
    if t == 'i':
        left, right = point
    elif t == 'p':
        left, right = unimodal_interval(offset, point, function)
    return golden_ratio(left, right, function, epsylon)
