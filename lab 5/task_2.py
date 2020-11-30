import numpy as np
from run import run

def r(t):
    return np.array([[0], [0]])

A = np.array([
    [0, 1],
    [-200, -102]
])
B = np.zeros_like(A)

x0 = np.array([[1], [-2]])

T = 0.1
t_max = 1.0

run(x0, A, B, r, T, t_max, print_every=1)