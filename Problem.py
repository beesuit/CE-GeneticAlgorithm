import random
import pqm
import numpy

class Problem(object):
    
    def __init__(self, name, solution_size, gene_range, p_type, pqm_type, solution=None):
        self.name = name
        self.solution_size = solution_size
        self.gene_range = gene_range
        self.p_type = p_type
        self.pqm_type = pqm_type
        self.solution = solution
        
    def calculate_fitness(self, c):
        raise NotImplementedError("The method hasn't been implemented yet.")
    
    def best(self, c1, c2):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
    def random_gene(self):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
    def random_chromossome(self):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class PqmProblem(Problem):
    
    def __init__(self, name, d, interval, p_type, X_train, X_test, y_train, y_test, solution=None):
        Problem.__init__(self, name, d, interval, p_type, solution)
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        
    
    def calculate_fitness(self, c):
        
        data_size = len(X_test)
        error = [0] * data_size
        fitness = 0
        
        for i in range(data_size):
            
           result = pqm.mem_retrieval_1cbit(X_test[i], X_train, c)
           
           if y_test[i] == '1':
               
               error[i] = result - y_test[i]
        
            elif y_test[i] == '0':
                
                error[i] =  - (y_test[i] - result)
                
        
        fitness = numpy.mean(error)
        
        return fitness
    
#    def check_solution(self, c):
#        if c.fitness == self.solution:
#            return True
#        return False
        
    def best(self, f1, f2):
        if f1 < f2:
            if self.p_type == 'MIN':
                return True
            else:
                return False
        elif self.p_type == 'MAX':
            return True
        else:
            return False
        
        
    def random_gene(self):
        return random.randint(0, 1)
    
    def random_chromossome(self):
        c = [self.random_gene() for x in range(self.solution_size)]
        random.shuffle(c)
        return c
        