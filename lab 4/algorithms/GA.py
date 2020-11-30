import numpy as np

class GeneticAlgorithm():
    def __init__(self, population_size, variables, restrictions, mutation_probability, function_evals, function, precision=16):
        self.population_size = population_size
        self.precision = precision
        self.restrictions = restrictions
        self.mutation_probability = mutation_probability
        self.function = function
        self.function_evals = function_evals
        self.population = self.make_population(population_size, restrictions, variables)

    def make_population(self, population_size, restrictions, variables):
        # population has to be a normal list for sorting purposes!
        pass
    
    def function_value(self, unit):
        pass
    
    def function_value_population(self):
        return [self.function_value(unit) for unit in self.population]

    def evaluate_population(self):
        return [self.evaluate_unit(unit) for unit in self.population]

    def evaluate_units(self, units):
        return [self.evaluate_unit(unit) for unit in units]

    def evaluate_unit(self, unit):
        return -self.function_value(unit)
    
    def check_boundaries(self, unit):
        return np.all(unit >= self.restrictions[0]) and np.all(unit <= self.restrictions[1])

    def mutate_unit(self, unit):
        pass

    def cross1(self, parents):
        pass

    def cross2(self, parents):
        pass
    
    def sort_population(self):
        self.population.sort(key=lambda unit: self.evaluate_unit(unit), reverse=True)
    
    def pick_fighters(self, units, amount):
        fighters = []
        indices = []
        for i in range(amount):
            index = int(np.random.random() * self.population_size)
            while index in indices:
                index = int(np.random.random() * self.population_size)
            indices.append(index)
            fighters.append(units[index])
        return np.array(fighters), indices

    def tournament(self, cross, amount):
        # Finds [amount] random units and removes worst and crosses two "random" as parents
        for i in range(self.function_evals):
            tournament_units, indices = self.pick_fighters(self.population, amount)
            tournament_goodness = self.evaluate_units(tournament_units)
            worst = np.argmin(tournament_goodness)
            worst = indices[worst]

            parents = []
            for unit, index in zip(tournament_units, indices):
                if index != worst:
                    parents.append(unit)
            parents = parents[:2]
            new_unit = self.cross1(parents) if cross == '1' else self.cross2(parents)
            new_unit = self.mutate_unit(new_unit)
            self.population[worst] = new_unit
