from functions import f1, Function
from nelder_mead import simplex
import numpy as np

def main():

    start1 = np.array([0.5, 0.5])
    start2 = np.array([20, 20])

    small_mins = []
    small_calls = []
    large_mins = []
    large_calls = []
    fun = Function(f1)
    for i in range(20):
        small_mins.append(simplex(start1, fun.call, offset=i+1))
        small_calls.append(fun.calls)
        fun.reset()
        large_mins.append(simplex(start2, fun.call, offset=i+1))
        large_calls.append(fun.calls)
        fun.reset()

    print("\tStart small\t\t\t\tStart big")
    for i in range(20):
        print("%d.\t%-25s - %d\t\t%-25s - %d" % (i+1, small_mins[i], small_calls[i], large_mins[i], large_calls[i]))