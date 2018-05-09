import Problem
import Crossover_op as C
import Mutation_op as M
import ParentSelection_op as P
import GenerationSelection_op as G
import Experiment as exp
import plot

class Chromossome(object):
    
    def __init__(self, chromossome):
        self.chromossome = chromossome
        self.fitness = float('inf')
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.chromossome == other.chromossome
    
    def __str__(self):
        return "%s, Fitness: %s" % (str(self.chromossome), str(self.fitness))
    
    def size(self):
        return len(self.chromossome)
    
class GA(object):
    
    def __init__(self, name, problem, crossover, mutation, parent_selection, generation_selection, pop_size=100, parents_n=50, limit=1000):
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
        
        self.best_solution = Chromossome([0])
        self.best_generation_solution = Chromossome([0])
        
    def init(self):
        self.best_solution = Chromossome([0])
        self.best_generation_solution = Chromossome([0])
    
    def init_pop(self):
        self.population.clear()
        for i in range(self.pop_size):
            c = self.problem.random_chromossome()
            chromossome = Chromossome(c)
            #Calculate fitness right after the chromossome is created
            chromossome.fitness = self.problem.calculate_fitness(chromossome.chromossome)
            
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
            #select parents
            parents = self.parent_selection.select_parents(self.population, self.parents_n, self.problem.best)
            #crossover and mutations
            children = self.crossover.crossover(parents)
            for c in children:
                self.mutation.mutation(c, self.problem.random_gene)
                #calculate children fitness
                c.fitness = self.problem.calculate_fitness(c.chromossome)
            
            #select new generation
            self.population = self.generation_selection.select_generation(self.population, children, self.pop_size)
            
            self.check_best()
            results.append(self.best_generation_solution.fitness)
            
            #check stop condition
            iteration += 1
        print(self.best_generation_solution)
        return results
    
    def check_best(self):
        sorted_population = sorted(self.population, key=self.sort_pop, reverse=self.maximization)
        
        if self.problem.best(sorted_population[0].fitness, self.best_generation_solution.fitness):
            
            self.best_generation_solution = sorted_population[0]
            
            if self.problem.best(self.best_generation_solution.fitness, self.best_solution.fitness):
                
                self.best_solution = self.best_generation_solution
                
                

if __name__ == "__main__":
    experiments = []
    
    #GA
    pop_size = 100
    parents_n = pop_size/2
    limit = 300
    
    #problem
    solution_size = 8
    gene_range = (0,solution_size-1)
    p_type = "MIN"
    
    #operator
    sample_size = 5
    mutation_rate = 0.1
    
    #executions
    n = 50
    
    problem = Problem.QueensProblem("8Queens", solution_size, gene_range, p_type)
    
    point_crossover = C.OnePointCrossover()
    uniform_crossover = C.UniformCrossover(p=0.5)
    
    #random_point_mutation = M.RandomPointMutation(mutation_rate)
    resetting_mutation = M.RandomResettingMutation(mutation_rate)
    swap_mutation = M.SwapMutation(mutation_rate)
    
    tournament_parent = P.ParentTournamentSelection(sample_size)
    uniform_parent = P.ParentUniformSelection(0.2)
    
    elitist_selection = G.ElitistSelection()
    robin_selection = G.RoundRobinSelection(sample_size)
    
    #1
#    algs = []
#    algs.append(GA("Variação alta", problem, uniform_crossover, resetting_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    algs.append(GA("Pressão evolutiva alta", problem, point_crossover, swap_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    
#    exps = []
#    for alg in algs: 
#        e = exp.Experiment(alg.name)
#        e.run(alg,n)
#        exps.append(e)
#    
#    plot.plot(exps, 'Extremos')
    
    #2
#    algs = []
#    algs.append(GA("Variação alta + elitismo", problem, uniform_crossover, resetting_mutation, uniform_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    algs.append(GA("Variação baixa - elitismo", problem, point_crossover, swap_mutation, tournament_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    
#    exps = []
#    for alg in algs: 
#        e = exp.Experiment(alg.name)
#        e.run(alg,n)
#        exps.append(e)
#    
#    plot.plot(exps, 'elitismo')
    
    #3
#    algs = []
#    algs.append(GA("Variação alta - Point Crossover", problem, point_crossover, resetting_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    algs.append(GA("Pressão evolutiva alta - Resetting Mutation", problem, point_crossover, resetting_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    
#    exps = []
#    for alg in algs: 
#        e = exp.Experiment(alg.name)
#        e.run(alg,n)
#        exps.append(e)
#    
#    plot.plot(exps, 'balanced')
    
    #4
#    algs = []
#    algs.append(GA("Pressão evolutiva alta", problem, point_crossover, swap_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    algs.append(GA("Variação alta + elitismo", problem, uniform_crossover, resetting_mutation, uniform_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    algs.append(GA("Pressão evolutiva alta - Resetting Mutation", problem, point_crossover, resetting_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
#    
#    exps = []
#    for alg in algs: 
#        e = exp.Experiment(alg.name)
#        e.run(alg,n)
#        exps.append(e)
#    
#    plot.plot(exps, '3best')
    
    #5
    algs = []
    algs.append(GA("Variação alta", problem, uniform_crossover, resetting_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Variação baixa - elitismo", problem, point_crossover, swap_mutation, tournament_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Variação alta - Point Crossover", problem, point_crossover, resetting_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    
    exps = []
    for alg in algs: 
        e = exp.Experiment(alg.name)
        e.run(alg,n)
        exps.append(e)
    
    plot.plot(exps, '3worst')
    
