import numpy as np
from matplotlib import pyplot as plt

from euler import euler
from euler_rev import euler_rev
from trapez import trapez
from pred_kor import pece, pecece
from runge_kutta import rk4

ALGORITHMS = ['Euler', 'Euler R', 'Trapez', 'Pece', 'Pecece', 'RK 4']

def print_state(xk, error, title='Current state', end="\n======\n\n"):
    print(title, end='\n\n')
    for i, alg in enumerate(ALGORITHMS):
        print(f"{alg}\t\t=> {xk[i].T}")
        if error is not None:
            print(f"Error\t\t=> {error[i].T}\n")
    
    print(end, end='')

def run(x0, A, B, r, T, t_max, f=None, print_every=100):
    pe = 0
    tk = 0
    xk = [
        x0, x0, x0, x0, x0, x0
    ]
    if f is not None:
        error = np.array([
            [[0],[0]], [[0],[0]], [[0],[0]], [[0],[0]], [[0],[0]], [[0],[0]]
        ])
    else:
        error = None
    xk_history = [
        x0,
        x0,
        x0,
        x0,
        x0,
        x0,
    ]
    while t_max - tk > 1e-6:
        pe += 1
        xk = np.array([
            euler(xk[0], tk, A, B, r, T),
            euler_rev(xk[1], tk, A, B, r, T),
            trapez(xk[2], tk, A, B, r, T),
            pece(xk[3], tk, A, B, r, T),
            pecece(xk[4], tk, A, B, r, T),
            rk4(xk[5], tk, A, B, r, T),
        ])
        for i in range(len(xk_history)):
            xk_history[i] = np.hstack((xk_history[i], xk[i]))
        if f is not None:
            error = error + np.absolute(f(tk, x0) - xk)
        if pe % print_every == 0:
            print_state(xk, error, title=f"Xks for time = {tk+T:.3f}")
        tk += T
    print_state(xk, error, title='Final', end='')
    for i, alg in enumerate(xk_history, 1):
        plt.subplot(3, 2, i, title=ALGORITHMS[i-1])
        plt.subplots_adjust(hspace=0.75)
        for i, var in enumerate(alg):
            plt.plot(var, label=f'x{i+1}')
        plt.legend()
    plt.show()
