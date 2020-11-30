import numpy as np

def calc_M(A, T):
    I = np.identity(A.shape[0])
    return I + T*A

def calc_N(B, T):
    return T*B

def euler(xk, tk, A, B, r, T):
    M = calc_M(A, T)
    N = calc_N(B, T)
    return M @ xk + N @ r(tk)