import random
import math

class Problem(object):
    
    def __init__(self, name, solution_size, gene_range, p_type):
        self.name = name
        self.solution_size = solution_size
        self.gene_range = gene_range
        self.p_type = p_type
        
    def calculate_fitness(self, c):
        raise NotImplementedError("The method hasn't been implemented yet.")
    
    def best(self, c1, c2):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
    def random_gene(self):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
    def random_chromossome(self):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class PQMProblem(Problem):
    
    def __init__(self, name, solution_size, precision, interval, p_type, pqm, X_test, y_test):
        Problem.__init__(self, name, solution_size, interval, p_type)
        self.X_test = X_test
        self.y_test = y_test
        self.pqm = pqm
        self.precision = precision
    
    def calculate_fitness(self, c):
        int_part = c[0:len(c)-self.precision]
        dec_part = c[len(c)-self.precision:]
        
        int_v = int(''.join(map(str, int_part)), 2)
        dec_v = int(''.join(map(str, dec_part)), 2)
        
        value = int_v + (dec_v/10**(len(str(dec_v))))
        scale_p = value
        
        data_size = len(self.X_test)
        error = 0
        fitness = float(math.inf)
        
        for i in range(data_size):
            
           result = self.pqm.classify(self.X_test[i], scale_p)
           
           if self.y_test[i] == self.pqm.pqm_class:
               
               error += (1 - result)**2
               
           elif self.y_test[i] != self.pqm.pqm_class:
               error += result**2
                
        fitness = error/data_size
        
        return fitness
        
    def best(self, f1, f2):
        compare = f1 < f2
    
        if self.p_type == 'MIN':
            return compare
        elif self.p_type == 'MAX':
            return not compare
        
    def random_gene(self):
        return random.randint(0, 1)
    
    def random_chromossome(self):
        c = [self.random_gene() for x in range(self.solution_size)]
        return c
    