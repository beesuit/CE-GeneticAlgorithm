class Chromossome(object):
    
    def __init__(self, chromossome):
        self.chromossome = chromossome
        self.fitness = float('inf')
        
    
    def __eq__(self, other):
        if other == None:
            return False
        
        return self.chromossome == other.chromossome
    
    def __str__(self):
        return "%s, Fitness: %s" % (str(self.chromossome[:10]), str(self.fitness))
    
    def size(self):
        return len(self.chromossome)
    
class GA(object):
    
    def __init__(self, name, problem, crossover, mutation, parent_selection, generation_selection, constraint=None,pop_size=100, parents_n=50, limit=1000):
        self.name = name
        self.population = []
        self.problem = problem
        self.maximization = (self.problem.p_type == "MAX")
        self.crossover = crossover
        self.mutation = mutation
        self.parent_selection = parent_selection
        self.generation_selection = generation_selection
        self.generation_selection.maximization = self.maximization
        self.pop_size = pop_size
        self.parents_n = parents_n
        self.limit = limit
        
        self.best_solution = None
        self.best_generation_solution = None
        
        self.constraint = constraint
        self.solutions = []
        
    def init(self):
        self.best_solution = None
        self.best_generation_solution = None
    
    def init_pop(self):
        self.population.clear()
        for i in range(self.pop_size):
            c = self.problem.random_chromossome()
            chromossome = Chromossome(c)
            #Calculate fitness right after the chromossome is created
            chromossome.fitness = self.__fitness(chromossome)
            
            self.population.append(chromossome)
            
    def sort_pop(self, c):
        return c.fitness
        
    def run(self):
        
        self.init()
        #initialize pop
        self.init_pop()
        
        iteration = 0
        results = []
        while iteration < self.limit:
            if iteration%100 == 0:
                print('Gen:',iteration)
            #select parents
            parents = self.parent_selection.select_parents(self.population, self.parents_n, self.problem.best)
            #crossover and mutations
            children = self.crossover.crossover(parents)
            for c in children:

                self.mutation.mutation(c, self.problem.random_gene)
                
                #fitness
                c.fitness = self.__fitness(c)
                
            
            #select new generation
            self.population = self.generation_selection.select_generation(self.population, children, self.pop_size)
            
            #print('PreviousBest', self.best_solution, self.__decode_solution(self.best_solution))
            self.check_best()
            #print('CurrentBest', self.best_solution, self.__decode_solution(self.best_solution))
            results.append(self.best_generation_solution.fitness)
            
            
            #check stop condition
            iteration += 1
        print(self.best_solution)
        return results
    
    # Check constraint and if the solution fitness has been already calculated
    def __fitness(self, c):
        #check constraint
        if self.constraint != None:
            self.constraint.constraint(c, self.problem.precision)
            
        # try:
        #     index = self.solutions.index(c)
        #     return self.solutions[index].fitness
        # except ValueError:
        #     #calculate children fitness
        #     self.solutions.append(c)
        return self.problem.calculate_fitness(c.chromossome)
    
    def __decode_solution(self, solution):
        result = None
        if solution != None:
            result = self.problem.decode_solution(solution.chromossome)
        
        return result
    
    def check_best(self):
        sorted_population = sorted(self.population, key=self.sort_pop, reverse=self.maximization)
        
        if self.best_generation_solution == None:
            self.best_generation_solution = sorted_population[0]
            self.best_solution = self.best_generation_solution
        
        else:
            if self.problem.best(sorted_population[0].fitness, self.best_generation_solution.fitness):
                
                self.best_generation_solution = sorted_population[0]
                
                if self.problem.best(self.best_generation_solution.fitness, self.best_solution.fitness):
                    
                    self.best_solution = self.best_generation_solution

