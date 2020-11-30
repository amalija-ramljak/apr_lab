from euler_rev import euler_impl
from trapez import trapez_impl
from euler import euler

def pece(xk, tk, A, B, r, T):
    xk1 = euler(xk, tk, A, B, r, T)
    return trapez_impl(xk, xk1, tk, A, B, r, T)

def pecece(xk, tk, A, B, r, T):
    xk1 = euler(xk, tk, A, B, r, T)
    xk1 = euler_impl(xk, xk1, tk, A, B, r, T)
    return euler_impl(xk, xk1, tk, A, B, r, T)