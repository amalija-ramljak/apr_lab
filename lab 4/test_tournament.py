from run import run
from functions import function_6
from algorithms.binary import BinaryGA
from algorithms.floating import FloatGA

import numpy as np

values = {
    'p': 50,
    'r': [-50, 150],
    'e': 10,
    'm': 0.1,
    'c': 10000,
    'v': 2,
    't': 3,
}

for t in range(3, 20):
    print(f"\nTournament size: {t}")
    values['t'] = t
    run(values, FloatGA, function_6, cross='2')