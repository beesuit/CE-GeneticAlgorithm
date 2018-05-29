import random
import math

class Problem(object):
    
    def __init__(self, name, solution_size, gene_range, p_type, solution=None):
        self.name = name
        self.solution_size = solution_size
        self.gene_range = gene_range
        self.p_type = p_type
        self.solution = solution
        
    def calculate_fitness(self, c):
        raise NotImplementedError("The method hasn't been implemented yet.")
    
    def best(self, c1, c2):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
    def random_gene(self):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
    def random_chromossome(self):
        raise NotImplementedError("The method hasn't been implemented yet.")
        
class FunctionProblem(Problem):
    
    def __init__(self, name, d, interval, p_type, function, solution=None):
        Problem.__init__(self, name, d, interval, p_type, solution)
        self.function = function
        
    def calculate_fitness(self, c):
        return self.function(c)
    
    def best(self, f1, f2):
        if f1 < f2:
            return True
        return False
    
    def random_gene(self):
        return random.uniform(self.gene_range[0], self.gene_range[1])
    
    def random_chromossome(self):
        c = [self.random_gene() for x in range(self.solution_size)]
        return c

class QueensProblem(Problem):
    
    def calculate_fitness(self, c):
        c_size = len(c)
        if c_size != self.solution_size:
            return float('inf')
        
        hits_count = 0
        for i in range(c_size):
            # [collum, left_diagonal, rigth_diagonal]
            hits = [False, False, False]
            for j in range(i+1, c_size):
                current_queen = c[i]
                next_queen = c[j]
                
                if next_queen == current_queen:
                    hits[0] = True
                elif next_queen == current_queen - (j - i):
                    hits[1] = True
                elif next_queen == current_queen + (j - i):
                    hits[2] = True
                
            for hit in hits:
                if hit:
                    hits_count += 1
        
        return hits_count
    
#    def check_solution(self, c):
#        if c.fitness == self.solution:
#            return True
#        return False
        
    def best(self, f1, f2):
        if f1 < f2:
            return True
        return False
        
    def random_gene(self):
        return random.randint(self.gene_range[0], self.gene_range[1])
    
    def random_chromossome(self):
        c = [x for x in range(self.solution_size)]
        random.shuffle(c)
        return c
        