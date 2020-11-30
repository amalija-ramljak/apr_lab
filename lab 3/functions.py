import numpy as np

class Function():
    def __init__(self, function, gradient, hesse):
        self.function = function
        self.gradient = gradient
        self.hesse = hesse
        self.call_count = 0
        self.gradient_count = 0
        self.hesse_count = 0
    
    def __call__(self, x):
        self.call_count += 1
        return self.function(x)
    
    def get_gradient(self, x):
        self.gradient_count += 1
        return self.gradient(x)
    
    def get_hesse(self, x):
        self.hesse_count += 1
        return self.hesse(x)
    
    def reset_calls(self):
        self.call_count = 0
        self.gradient_count = 0
        self.hesse_count = 0

# Rosenbrock banana

def f1(x):
    return 100 * (x[1,0] - x[0,0]**2)**2 + (1 - x[0,0])**2

def f1_gradient(x):
    x1 = x[0,0]
    el = x[1,0] - x1**2
    return np.array([
        [-400*x1*el - 2*(1 - x1)],
        [200*el]
    ])

def f1_hesse(x):
    x1 = x[0,0]
    return np.array([
        [2-400*x[1,0]+1200*x1**2, -400*x1],
        [-400*x1, 200]
    ])

# Funkcija 2

def f2(x):
    return (x[0,0] - 4)**2 + 4*(x[1,0] - 2)**2

def f2_gradient(x):
    return np.array([
        [2*(x[0,0]-4)],
        [8*(x[1,0]-2)]
    ])

def f2_hesse(x):
    return np.array([[2, 0],[0, 8]])

# Funkcija 3

def f3(x):
    return (x[0,0] - 2)**2 + (x[1,0] + 3)**2

def f3_gradient(x):
    return np.array([
        [2*(x[0,0]-2)],
        [2*(x[1,0]+3)]
    ])

def f3_hesse(x):
    return np.array([[2, 0],[0, 2]])

# Funkcija 4

def f4(x):
    return (x[0,0] - 3)**2 + x[1,0]**2

def f4_gradient(x):
    return np.array([
        [2*(x[0,0]-3)],
        [2*x[1,0]]
    ])

def f4_hesse(x):
    return np.array([[2, 0],[0, 2]])
