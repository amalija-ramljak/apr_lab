from run import run
from functions import *
from algorithms.binary import BinaryGA

import numpy as np

values = {
    'p': 200,
    'r': [-50, 150],
    'e': 5,
    'm': 0.2,
    'c': 50000,
    'v': 2,
    't': 3,
}

print("Running function 1")
print("Single random breakpoint")
run(values, BinaryGA, function_1)
print("Random copy-parent switching")
run(values, BinaryGA, function_1, cross='2')

print("\nRunning function 6")
print("Single random breakpoint")
run(values, BinaryGA, function_6)
print("Random copy-parent switching")
run(values, BinaryGA, function_6, cross='2')

print("\nRunning function 7")
print("Single random breakpoint")
run(values, BinaryGA, function_7)
print("Random copy-parent switching")
run(values, BinaryGA, function_7, cross='2')

values['v'] = 5
print("\nRunning function 3")
print("Single random breakpoint")
run(values, BinaryGA, function_3)
print("Random copy-parent switching")
run(values, BinaryGA, function_3, cross='2')