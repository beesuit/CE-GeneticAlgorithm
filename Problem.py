import random
import math
import numpy as np

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

class CutProblem(Problem):

    def __init__(self, name, n_windows, window_w, window_h, bar_length):
        solution_size = 4 * n_windows
        gene_range = (0,1)
        p_type = 'MIN'
        Problem.__init__(self, name, solution_size, gene_range, p_type)

        self.n_windows = n_windows
        self.window_w = window_w
        self.window_h = window_h
        self.bar_length = bar_length

        self.representation = {0: self.window_w, 1: self.window_h}
    
    def calculate_fitness(self, c):
        bar = self.bar_length
        waste = 0

        self.__validate_chromossome(c)

        for g in c:
            cut_length = self.representation[g]

            if bar < cut_length:
                waste += bar
                bar = self.bar_length
            
            bar -= cut_length

        waste += bar

        return waste

    def best(self, c1, c2):
        compare = c1 < c2
        if self.p_type == 'MIN':
            return compare
        elif self.p_type == 'MAX':
            return not compare
    
    def random_gene(self):
        return random.randint(0,1)

    def __validate_chromossome(self, c):
        unique_values, counts = np.unique(c, return_counts=True)
        balanced_count = self.solution_size/len(unique_values)
        max_count = counts.max()

        if max_count > balanced_count:
            #raise Exception
            value = unique_values[counts.argmax()]
            other_value = unique_values[counts.argmin()]
            indices = np.where(np.array(c) == value)[0]

            change_indices = np.random.choice(indices, int(max_count-balanced_count), replace=False)

            for i in change_indices:
                c[i] = other_value

    def random_chromossome(self):
        c = [x%2 for x in range(self.solution_size)]
        random.shuffle(c)

        return c
    
    def decode_solution(self, c):
        return [self.representation[x] for x in c]

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
    