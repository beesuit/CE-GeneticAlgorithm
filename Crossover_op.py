from GA import Chromossome
import random

class Crossover(object):
    
    def crossover(self, parents):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class OnePointCrossover(Crossover):
    
    def crossover(self, parents):
        children = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            
            parent_length = len(parent1.chromossome)
            cross_point = random.randint(1, parent_length-1)
            
            child1 = Chromossome(parent1.chromossome[:cross_point] + parent2.chromossome[cross_point:])
            child2 = Chromossome(parent2.chromossome[:cross_point] + parent1.chromossome[cross_point:])
            
            children.append(child1)
            children.append(child2)
            
        return children
    
class UniformCrossover(Crossover):
    
    def __init__(self, p=0.5):
        Crossover.__init__(self)
        self.p = p
    
    def crossover(self, parents):
        children = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            parent_length = len(parent1.chromossome)
            p_list = [random.random() for x in range(parent_length)]
            
            child_c1 = []
            child_c2 = []
            
            for j in range(parent_length):
                if p_list[j] < self.p:
                   child_c1.append(parent1.chromossome[j])
                   child_c2.append(parent2.chromossome[j])
                else:
                   child_c1.append(parent2.chromossome[j])
                   child_c2.append(parent1.chromossome[j])
            
            child1 = Chromossome(child_c1)
            child2 = Chromossome(child_c2)

            children.append(child1)
            children.append(child2)
            
        return children