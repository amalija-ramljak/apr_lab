import numpy as np

def calc_P(A, T):
    I = np.identity(A.shape[0])
    return np.linalg.inv(I - T*A)

def calc_Q(A, T, B):
    I = np.identity(A.shape[0])
    inv = np.linalg.inv(I - T*A)
    return T * inv @ B

def euler_rev(xk, tk, A, B, r, T):
    P = calc_P(A, T)
    Q = calc_Q(A, T, B)
    return P @ xk + Q @ r(tk)

def euler_impl(xk, xk1, tk, A, B, r, T):
    return xk + T * (A @ xk1 + B @ r(tk+T))