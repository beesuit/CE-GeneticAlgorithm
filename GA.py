import random

class Chromossome(object):
    
    def __init__(self, chromossome):
        self.chromossome = chromossome
        self.fitness = float('inf')
    
    def __eq__(self, other):
        return self.chromossome == other.chromossome
    
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __str__(self):
        return "%s, Fitness: %s" % (str(self.chromossome), str(self.fitness))
    
    def size(self):
        return len(self.chromossome)
    
class GA(object):
    
    def __init__(self, problem, crossover, mutation, parent_selection, pop_size=100, limit=10000):
        self.population = []
        self.problem = problem
        self.crossover = crossover
        self.mutation = mutation
        self.parent_selection = parent_selection
        self.pop_size = pop_size
        self.limit = limit
        
    def init_pop(self):
        solution_size = self.problem.solution_size
        for i in range(self.pop_size):
            chromossome = [x for x in range(solution_size)]
            random.shuffle(chromossome)
            chrom = Chromossome(chromossome)
            #Calculate fitness right after the chromossome is created
            chrom.fitness = self.problem.calculate_fitness(chrom)
            self.population.append(chrom)
        
    def run(self):
        #initialize pop
        init_pop()
        
        iteration = 0
        while iteration < self.limit:
            #select parents
            parents = self.parent_selection.select_parents(self.population)
            #crossover and mutations
            children = self.crossover.crossover(parents)
            for c in children:
                self.mutation.mutation(c)
                #calculate children fitness
                c.fitness = self.problem.calculate_fitness(c)
        
            #select new generation
            #TODO newgen_op
            #select_newgen(population, children)
            #check stop conditions
#            iteration += 1
#            solution = check_solution(population)
#            if solution is not None:
#                print("Iteration: ",iteration)
#                return solution

def init_pop(pop_size, chromossome_size):
    population = []
    for i in range(pop_size):
        chromossome = [x for x in range(chromossome_size)]
        random.shuffle(chromossome)
        chrom = Chromossome(chromossome)
        population.append(chrom)
    return population

def calculate_fitness(population):
    for individual in population:
        chrom = individual.chromossome
        hits_count = 0
        for i in range(len(chrom)):
            # [collum, left_diagonal, rigth_diagonal]
            hits = [False, False, False]
            for j in range(i+1, len(chrom)):
                current_queen = chrom[i]
                next_queen = chrom[j]
                
                if next_queen == current_queen:
                    hits[0] = True
                elif next_queen == current_queen - (j - i):
                    hits[1] = True
                elif next_queen == current_queen + (j - i):
                    hits[2] = True
                
            for hit in hits:
                if hit:
                    hits_count += 1
        
        individual.fitness = hits_count

def select_parents(population, sample_size):
    parents = []
    indices = [x for x in range(len(population))]
    random.shuffle(indices)
    
    while(len(indices) >= sample_size):
        sample = indices[0:sample_size]
        del indices[0:sample_size]
        
        candidates = []
        for i in sample:
            candidates.append(population[i])
            
        candidates = sorted(candidates)
        parents.extend(candidates[0:2])
        
    return parents

def crossover(parents):
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

def mutation(children, mutation_rate, upper_bound):
    for child in children:
        for i in range(len(child.chromossome)):
            if random.random() <= mutation_rate:
                child.chromossome[i] = random.randint(0, upper_bound)
                
def select_newgen(population, childs):
    pop_size = len(population)
    population.extend(childs)
    population = sorted(population)
    
    return population[:pop_size]

def check_solution(population):
    for individual in population:
        if individual.fitness == 0:
            return individual

def main_loop():
    pop_size = 100
    chromossome_size = 8
    upper_bound = chromossome_size - 1
    sample_size = 5
    mutation_rate = 0.1
    limit = 10000
    #initialize pop
    population = init_pop(pop_size, chromossome_size)
    #calculate pop fitness
    calculate_fitness(population)
    
    iteration = 0
    while iteration < limit:
        #select parents
        parents = select_parents(population, sample_size)
        #crossover and mutations
        children = crossover(parents)
        mutation(children, mutation_rate, upper_bound)
        #calculate children fitness
        calculate_fitness(children)
        #select new generation
        select_newgen(population, children)
        #check stop conditions
        iteration += 1
        solution = check_solution(population)
        if solution is not None:
            print("Iteration: ",iteration)
            return solution

print(main_loop())