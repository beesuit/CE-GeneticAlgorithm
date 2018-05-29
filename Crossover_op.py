from GA import Chromossome
import random

class Crossover(object):
    
    def crossover(self, parents):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class ArithmeticCrossover(Crossover):
    
    def crossover(self, parents):
        children = []
        for i in range(0, len(parents), 2):
            parent1_c = parents[i].chromossome
            parent2_c = parents[i+1].chromossome
            child_c1 = parent1_c[:]
            child_c2 = parent2_c[:]
            
            parent_length = len(parent1_c)
            
            k = random.randint(0, parent_length-1)
            
            mean = (parent1_c[k]+parent2_c[k])/2
            child_c1[k] = mean
            child_c2[k] = mean
            
            child1 = Chromossome(child_c1)
            child2 = Chromossome(child_c2)
            
            children.append(child1)
            children.append(child2)
            
        return children
        
class WholeArithmeticCrossover(Crossover):
    
    def crossover(self, parents):
        children = []
        for i in range(0, len(parents), 2):
            alpha = random.random()
            
            parent1_c = parents[i].chromossome
            parent2_c = parents[i+1].chromossome
            child_c1 = []
            child_c2 = []
            
            parent_length = len(parent1_c)
            
            for j in range(parent_length):
                child_c1.append(alpha*parent1_c[j]+(1-alpha)*parent2_c[j])
                child_c2.append(alpha*parent2_c[j]+(1-alpha)*parent1_c[j])
                
            child1 = Chromossome(child_c1)
            child2 = Chromossome(child_c2)
            
            children.append(child1)
            children.append(child2)
            
        return children
        
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