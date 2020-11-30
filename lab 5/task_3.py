import numpy as np
from run import run

def r(t):
    return np.array([[1], [1]])

A = np.array([
    [0, -2],
    [1, -3],
])
B = np.array([
    [2, 0],
    [0, 3],
])

x0 = np.array([[1], [3]])

T = 0.01
t_max = 10.0

run(x0, A, B, r, T, t_max)
