from functions import *
from nelder_mead import simplex
from hooke_jeeves import hooke_jeeves

import numpy as np
from numpy import random


def main():
    fun = Function(f6)
    tolerance = 1e-4
    total_runs = 100
    succeeded = 0
    for i in range(total_runs):
        x = np.array([random.random() * 100 - 50, random.random() * 101 - 50])
        print("\nRun", i+1)
        print("Start", x)
        xmin = simplex(x, fun.call)
        print("Argmin", xmin)
        funmin = fun.call(xmin)
        print("Valmin %f" % funmin)
        if funmin < tolerance:
            succeeded += 1
        fun.reset()

    print("\n\nTotal", total_runs)
    print("Succeded", succeeded)
    print("Odds of finding the global optimum", succeeded/total_runs)

main()