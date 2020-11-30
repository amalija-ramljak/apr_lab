import numpy as np

def run(values, algorithm, function, cross='1'):
    # population_size p, variables v, restrictions r, mutation_probability m, function_evals f, function
    # precision (binary length) - 16
    model = algorithm(values['p'], values['v'], values['r'], values['m'], values['c'], function)
    model.tournament(cross=cross, amount=values['t'])
    evals = model.evaluate_population()
    best = model.population[np.argmax(evals)]
    minimum = model.function_value(best)
    print(f"\tThe minimum: {minimum:.{values['e']}f}")
    print("\tFound it? " + ("Yes!" if minimum < 1e-6 else "Nope."))