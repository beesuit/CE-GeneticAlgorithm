import random

class Mutation(object):
    
    def __init__(self, p):
        self.p = p
    
    def mutation(self, c):
        raise NotImplementedError("The method hasn't been implemented yet.")

class RandomResettingMutation(Mutation):
    
    def mutation(self, c, gene_generator):
        for g in range(c.size()):
            if random.random() < self.p:
                c.chromossome[g] = gene_generator()

class SwapMutation(Mutation):
    
    def mutation(self, c, gene_generator):
        if random.random() < self.p:
            point1 = random.randint(0, c.size()-1)
            point2 = random.randint(0, c.size()-1)
            value1 = c.chromossome[point1]
            value2 = c.chromossome[point2]
            
            c.chromossome[point1] = value2
            c.chromossome[point2] = value1
            

class RandomPointMutation(Mutation):
    
    def mutation(self, c, gene_generator):
        if random.random() < self.p:
            point = random.randint(0, c.size()-1)
            c.chromossome[point] = gene_generator()
                