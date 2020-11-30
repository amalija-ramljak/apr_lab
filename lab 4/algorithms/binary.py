import numpy as np
from algorithms.GA import GeneticAlgorithm

class BinaryGA(GeneticAlgorithm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def make_population(self, population_size, restrictions, variables):
        # population has to be a normal list for sorting purposes!
        population = []
        for _ in range(population_size):
            unit = 2**self.precision * np.random.random(variables)
            population.append(unit.astype(int))
        return np.array(population)
    
    def function_value(self, unit):
        return self.function(self.turn_to_number(unit))
    
    def int_to_bin(self, unit):
        bin_unit = []
        for var in unit:
            bin_var = bin(var)[2:]
            if len(bin_var) < self.precision:
                padding = self.precision * '0'
                bin_var = padding + bin_var
            bin_unit.append(bin_var)
        return np.array(bin_unit)

    def turn_to_number(self, unit):
        nums = []
        for u in unit:
            nums.append(u / 2**self.precision)
        nums = np.array(nums)
        return self.restrictions[0] + nums * (self.restrictions[1] - self.restrictions[0])

    def mutate_unit(self, unit):
        # uniform mutation
        if np.random.random() < self.mutation_probability:
            return (2**self.precision * np.random.random(unit.shape)).astype(int)
        return unit

    def cross1(self, parents):
        # single point crossover, same mask for all variables
        mask_index = int(0.3 * self.precision)
        mask = 2**mask_index - 1
        child = parents[0] & mask | parents[1] & ~mask
        return child if self.check_boundaries(self.turn_to_number(child)) else self.cross1(parents)

    def cross2(self, parents):
        parents = [self.int_to_bin(parents[0]), self.int_to_bin(parents[1])]
        current_parent = parents[0]
        parent_index = 0
        child = []
        for i in range(len(current_parent)):
            parent_switch_rate = np.random.random()
            var = ''
            for j in range(self.precision):
                var += current_parent[i][j]
                check_switch = np.random.random()
                if check_switch <= parent_switch_rate:
                    current_parent = parents[1 - parent_index]
                    parent_index = 1 - parent_index
            child.append(int(var, 2))
        return np.array(child) if self.check_boundaries(self.turn_to_number(child)) else self.cross2(parents)