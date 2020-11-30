import numpy as np
from math import sin

class Function():
    def __init__(self, function):
        self.function = function
        self.calls = 0

    def call(self, x):
        self.calls += 1
        return self.function(x)
    
    def reset(self):
        self.calls = 0

def assert_dimension(x, dim):
    return x.shape[0] == dim

def f1(x):
    if not assert_dimension(x, 2):
        print("The banana has an exclusively 2D input!")
        return None
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def f2(x):
    if not assert_dimension(x, 2):
        print("The 2nd function has an exclusively 2D input!")
        return None
    return (x[0] - 4)**2 + 4 * (x[1] - 2)**2

def f3(x):
    i = np.arange(1, len(x)+1)
    return np.sum((x-i)**2)

def f4(x):
    if not assert_dimension(x, 2):
        print("Jakob fun has an exclusively 2D input!")
        return None
    return abs(x[0]**2 - x[1]**2) + np.linalg.norm(x)

def f6(x):
    norma = np.linalg.norm(x)
    return 0.5 + (sin(norma)**2 - 0.5) / (1 + 0.001 * norma**2)**2