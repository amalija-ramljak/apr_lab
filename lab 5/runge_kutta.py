import numpy as np

def f(x, t, A, B, r):
    return A @ x + B @ r(t)

def rk4(xk, tk, A, B, r, T):
    m1 = f(xk, tk, A, B, r)
    m2 = f(xk+0.5*T*m1, tk+0.5*T, A, B, r)
    m3 = f(xk+0.5*T*m2, tk+0.5*T, A, B, r)
    m4 = f(xk+T*m3, tk+T, A, B, r)
    return xk + (T/6) * (m1 + 2*m2 + 2*m3 + m4)