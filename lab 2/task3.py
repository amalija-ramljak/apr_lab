from functions import f4
from hooke_jeeves import hooke_jeeves
from nelder_mead import simplex
import numpy as np

def main():
    start = np.array([5.0, 5.0])
    hj_min = hooke_jeeves(start, f4)
    sp_min = simplex(start, f4)
    print("Hooke-Jeeves")
    print("argmin", hj_min)
    print("valmin", f4(hj_min))
    print("\nNelder-Meade")
    print("argmin", sp_min)
    print("valmin", f4(sp_min))