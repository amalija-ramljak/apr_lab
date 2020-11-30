from run import run
from functions import *
from algorithms.floating import FloatGA

import numpy as np

values = {
    'p': 150,
    'r': [-50, 150],
    'e': 5,
    'm': 0.1,
    'c': 25000,
    'v': 2,
    't': 3,
}

print("Running function 1")
print("Arithmetic cross")
run(values, FloatGA, function_1)
print("Heuristic cross")
run(values, FloatGA, function_1, cross='2')

print("\nRunning function 6")
print("Arithmetic cross")
run(values, FloatGA, function_6)
print("Heuristic cross")
run(values, FloatGA, function_6, cross='2')

print("\nRunning function 7")
print("Arithmetic cross")
run(values, FloatGA, function_7)
print("Heuristic cross")
run(values, FloatGA, function_7, cross='2')

values['v'] = 5
print("\nRunning function 3")
print("Arithmetic cross")
run(values, FloatGA, function_3)
print("Heuristic cross")
run(values, FloatGA, function_3, cross='2')