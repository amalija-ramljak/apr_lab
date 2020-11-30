import numpy as np
from run import run

def x_t(t, x0):
    x1 = x0[0] * np.cos(t) + x0[1] * np.sin(t)
    x2 = x0[1] * np.cos(t) - x0[0] * np.sin(t)
    return np.array([x1, x2])

def r(t):
    return np.array([[0], [0]])

x0 = np.array([[1], [1]])

A = np.array([
    [0, 1],
    [-1, 0],
])
B = np.zeros_like(A)

T = 0.01
t_max = 10.0

run(x0, A, B, r, T, t_max, f=x_t)
