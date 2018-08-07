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
    
    def decode_solution(self, c): 
        raise NotImplementedError("The method hasn't been implemented yet.")

class WLNNProblem(Problem):
    
    def __init__(self, name, solution_size, precision, interval, p_type, wlnn, X_test, y_test):
        solution_size = precision*wlnn.neurons_n
        Problem.__init__(self, name, solution_size, interval, p_type)
        self.X_test = X_test
        self.y_test = y_test
        self.wlnn = wlnn
        self.precision = precision
    
    def calculate_fitness(self, c):
        params = self.decode_solution(c)
        
        test_size = len(self.X_test)
        
        hit = 0
        for i in range(test_size):
           result = self.wlnn.classify(self.X_test[i], params)
           
           if result == self.y_test[i]:
               hit += 1
               
        accuracy = hit/test_size
        
        return accuracy
        
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
    
    def decode_solution(self, c): 
        params = []
        
        for i in range(self.wlnn.neurons_n):
            start = i*self.precision
            end = start+self.precision
            
            param_b = c[start:end]
            
            dec_v = int(''.join(map(str, param_b)), 2)
            param = dec_v/10**(len(str(dec_v)))
            
            params.append(param)
        
        return params
     
class PQMLinearApoxProblem(Problem):
    
    def __init__(self, name, solution_size, precision, interval, p_type, pqms, X_test, y_test):
        Problem.__init__(self, name, solution_size, interval, p_type)
        self.X_test = X_test
        self.y_test = y_test
        self.pqms = pqms
        self.precision = precision
    
    def calculate_fitness(self, c):
        params = self.decode_solution(c)
        
        sum_errors = 0
        for i in range(len(self.pqms)):
            result = self.pqms[i].classify(self.X_test, params[i])
            
            result = 1 - result
       
            error = (self.y_test - result)**2
            sum_errors += error
            
        fitness = sum_errors/len(self.pqms)
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
    
    def decode_solution(self, c): 
        params = []
        
        for i in range(len(self.pqms)):
            start = i*self.precision
            end = start+self.precision
            
            param_b = c[start:end]
            
            dec_v = int(''.join(map(str, param_b)), 2)
            param = dec_v/10**(len(str(dec_v)))
            
            params.append(param)
        
        return params
       
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
    