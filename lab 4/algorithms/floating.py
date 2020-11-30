import numpy as np
from algorithms.GA import GeneticAlgorithm

class FloatGA(GeneticAlgorithm):
    def make_population(self, population_size, restrictions, variables):
        lower = restrictions[0]
        upper = restrictions[1]
        pop = []
        for i in range(population_size):
            unit = lower+(upper-lower)*np.random.random(variables)
            pop.append(unit)
        return pop
    
    def function_value(self, unit):
        return self.function(unit)

    def mutate_unit(self, unit):
        if np.random.random() < self.mutation_probability:
            return unit + np.random.random(unit.shape)*0.5
        return unit

    def cross1(self, parents):
        a = np.random.random(len(parents[0]))
        child = a*parents[0] + (1-a)*parents[1]
        return child if self.check_boundaries(child) else self.cross1(parents)

    def cross2(self, parents):
        parent_evals = self.evaluate_units(parents)
        better = np.argmax(parent_evals)
        a = np.random.random()
        child = a * (parents[better] - parents[1-better]) + parents[better]
        return child