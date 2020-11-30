import numpy as np

def calc_R(A, T):
    I = np.identity(A.shape[0])
    inv = np.linalg.inv(I - A * (T/2))
    m = I + A * (T/2)
    return inv @ m

def calc_S(A, B, T):
    I = np.identity(A.shape[0])
    inv = np.linalg.inv(I - A * (T/2))
    return T * 0.5 * inv @ B

def trapez(xk, tk, A, B, r, T):
    R = calc_R(A, T)
    S = calc_S(A, B, T)
    return R @ xk + S @ (r(tk) + r(tk+T))

def trapez_impl(xk, xk1, tk, A, B, r, T):
    return xk + 0.5 * T * (A @ xk + B @ r(tk) + A @ xk1 + B @ r(tk+T))