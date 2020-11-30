from algorithms.binary import BinaryGA
from algorithms.floating import FloatGA
from run import run as run_genetic
from functions import *

import numpy as np
    

PARAMETERS = {
    'p': 'Population size',
    'd': 'Result display [binary, float]',
    'e': 'Precision (decimals count)',
    'm': 'Mutation probability',
    'c': 'Maximum function evaluations allowed',
    'r': 'Upper and lower boundaries',
    'v': 'Number of variables',
    'f': 'Function used (f1, f3, f6, f7)',
    't': 'Tournament size',
}

VALUES = {
    'p': 150,
    'd': 'float',
    'r': [-50, 150],
    'e': 5,
    'm': 0.1,
    'c': 20000,
    'v': 2,
    'f': 'f1',
    't': 3,
}

TYPES = {
    'int': 'pevtc',
    'float': 'm',
    'str': 'df',
    'rng': 'r'
}

FUNCTIONS = {
    'f1': function_1,
    'f3': function_3,
    'f6': function_6,
    'f7': function_7,
}

change = input("Want to change some parameters? [y/n]: ") in 'yes|Yes'
if change:
    print("Parameter keys:")
    for p in PARAMETERS:
        print("\t" + p + ' - ' + PARAMETERS[p] + ' (' + str(VALUES[p]) + ')')
    print("\ta - All parameters")
    parameters = input("List the parameter keys you wish to input: ")
    if parameters == 'a':
        parameters = 'pdmeftrv'
    for p in parameters:
        if p == 'a':
            print("Sorry, 'a' does not go with others!")
        value = input('\t' + PARAMETERS[p] + " value: ")
        if p in TYPES['int']:
            VALUES[p] = int(value)
        elif p in TYPES['float']:
            VALUES[p] = float(value)
        elif p in TYPES['str']:
            VALUES[p] = value
        elif p in TYPES['rng']:
            value = value.split(' ')
            VALUES[p] = [int(v) for v in value]
            
print("All right! The values used will be:")
for p in VALUES:
    print("\t" + PARAMETERS[p] + ":", VALUES[p])

algorithm = BinaryGA if VALUES['d'] == 'binary' else FloatGA

run_genetic(VALUES, algorithm, FUNCTIONS[VALUES['f']])