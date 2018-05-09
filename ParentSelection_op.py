import random

class ParentSelection(object):
    
    def select_parents(self, population, n, best_f):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class ParentTournamentSelection(ParentSelection):
    
    def __init__(self, sample_size):
        ParentSelection.__init__(self)
        self.sample_size = sample_size
        
    def select_parents(self, population, n, best_f):
        pop_size = len(population)
        
        parents = []
        while len(parents) < n:
            best = None
            for j in range(self.sample_size):
                sample = population[random.randint(0, pop_size-1)]
                
                if best == None:
                    best = sample
                elif best_f(sample.fitness, best.fitness):
                    best = sample
            
            parents.append(best)
            
        return parents
    
class ParentUniformSelection(ParentSelection):
    
    def __init__(self, prob):
        ParentSelection.__init__(self)
        self.prob = prob
        
    def select_parents(self, population, n, best_f):
        pop_size = len(population)
        parents = []
        
        i = 0
        while len(parents) < n:
            if random.random() < self.prob:
                parents.append(population[i])
            
            if i < pop_size-1:
                i+=1
            else:
                i=0
            
        return parents
            