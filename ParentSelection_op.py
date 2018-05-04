import random

class ParentSelection(object):
    
    def select_parents(self, population):
        raise NotImplementedError("Method hasn't been implemented.")
        
class ParentTournamentSelection(ParentSelection):
    
    def __init__(self, sample_size):
        ParentSelection.__init__(self)
        self.sample_size = sample_size
        
    def select_parents(self, population):
        pop_size = len(population)
        parents = []
        
        for i in range(pop_size):
            best = None
            for j in range(self.sample_size):
                sample = population[random.randint(0, pop_size-1)]
                
                if best == None:
                    best = sample
                else:
                    #TODO Try a Fitness object
                    if sample.fitness > best.fitness:
                        best = sample
            
            parents.append(best)
        
        return parents
            