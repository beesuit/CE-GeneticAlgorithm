import random

class GenerationSelection(object):
    
    def __init__(self, maximize=False):
        self.maximize = maximize 
    
    def sort_pop(self, c):
        return c.fitness    
    
    def select_generation(self, population, children, pop_size):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class ElitistSelection(GenerationSelection):
    
    def select_generation(self, population, children, pop_size):
        population.extend(children)
        
        return sorted(population, key=self.sort_pop, reverse=self.maximize)[:pop_size]
    
class RoundRobinSelection(GenerationSelection):
    
    def __init__(self, sample_size):
        GenerationSelection.__init__(self)
        self.sample_size = sample_size
    
    def select_generation(self, population, children, pop_size):
        population.extend(children)
        
        survivors = []
        while len(survivors) < pop_size:
            sample = random.sample(population, self.sample_size)
            best = sorted(sample, key=self.sort_pop, reverse=self.maximize)[0]
            survivors.append(best)
        
        return survivors
    
    
    
    