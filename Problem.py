import random

class Problem(object):
    
    def __init__(self, name, solution_size, solution, gene_range):
        self.name = name
        self.solution_size = solution_size
        self.solution = solution
        self.gene_range = gene_range
    
    def calculate_fitness(self, c):
        raise NotImplementedError("Method hasn't been implemented.")
    
    def check_solution(self, c):
        raise NotImplementedError("Method hasn't been implemented.")
        
    def random_gene(self):
        raise NotImplementedError("Method hasn't been implemented.")

class QueensProblem(Problem):
    
    def calculate_fitness(self, c):
        c_size = c.size()
        if c_size != self.solution_size:
            return 0
        
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
    
    def check_solution(self, c):
        if c.fitness == self.solution:
            return True
        return False
    
    def random_gene(self):
        return random.randint(self.gene_range[0], self.gene_range[1])