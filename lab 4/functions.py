import numpy as np

def function_1(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def function_3(x):
    return sum([(e-i)**2 for i, e in enumerate(x, 1)])

def function_6(x):
    result = 0.5
    sum_sq = np.sum([e*e for e in x])
    sine = np.sin(np.sqrt(sum_sq))**2
    result += (sine - 0.5)/(1 + 0.001 * sum_sq)**2
    return result

def function_7(x):
    sum_sq = np.sum([e*e for e in x])
    return sum_sq**0.25 * (1 + np.sin(50*sum_sq**0.1)**2)