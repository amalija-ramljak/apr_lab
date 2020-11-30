import numpy as np
from run import run

def r(t):
    return np.array([[t], [t]])

A = np.array([
    [1, -5],
    [1, -7],
])
B = np.array([
    [5, 0],
    [0, 3],
])

x0 = np.array([[-1], [3]])

T = 0.01
t_max = 1.0

run(x0, A, B, r, T, t_max, print_every=10)
