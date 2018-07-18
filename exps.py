import Problem
import Crossover_op as C
import Mutation_op as M
import ParentSelection_op as P
import GenerationSelection_op as G
import Experiment as exp
import plot
import function as f
from GA import GA


def pqm_opt():
    experiments = []
    
    #GA
    pop_size = 100
    parents_n = pop_size/2
    limit = 300
    
    #problem2
    solution_size = 3
    gene_range = (0,1)
    p_type = "MAX"
    
    function = f.rosenbrock
    
    #operator
    sample_size = 5
    mutation_rate = 0.1
    
    #executions
    #n = 50
    n=1
    
    #problem = Problem.QueensProblem("8Queens", solution_size, gene_range, p_type)
    problem = Problem.FunctionProblem("Sphere", solution_size, gene_range, p_type, function)
    
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

def exp1(name, function, pop_size, limit, n):
    #GA
    #pop_size = 100
    parents_n = pop_size/2
    #limit = 100
    
    #problem
    solution_size = 15
    gene_range = (-5,10)
    p_type = "MIN"
    
    #operator parameters
    sample_size = 5
    mutation_rate = 0.1
    step = 0.4
    
    #executions
    #n=1
    
    problem = Problem.FunctionProblem(name, solution_size, gene_range, p_type, function)
    
    a_crossover = C.ArithmeticCrossover()
    wa_crossover = C.WholeArithmeticCrossover()
    
    uf_mutation = M.UniformMutation(mutation_rate)
    nuf_mutation = M.NonuniformMutation(mutation_rate, step)
    
    
    tournament_parent = P.ParentTournamentSelection(sample_size)
    uniform_parent = P.ParentUniformSelection(0.2)
    
    elitist_selection = G.ElitistSelection()
    robin_selection = G.RoundRobinSelection(sample_size)
    
    #1 wa | 
    title = name + '| wa_crossover | Mutation: Uniform vs Nonuniform'
    algs = []
    algs.append(GA("Uniform - Elitism", problem, wa_crossover, uf_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform - Elitism", problem, wa_crossover, nuf_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Uniform - Diversity", problem, wa_crossover, uf_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform - Diversity", problem, wa_crossover, nuf_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))

    run(algs, n, title)
    
    #2 a |
    title = name + '| a_crossover | Mutation: Uniform vs Nonuniform'
    algs = []
    algs.append(GA("Uniform - Elitism", problem, a_crossover, uf_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform - Elitism", problem, a_crossover, nuf_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Uniform - Diversity", problem, a_crossover, uf_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform - Diversity", problem, a_crossover, nuf_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    
    run(algs, n, title)
    
def exp3(name, function, pop_size, limit, n):
    #GA
    #pop_size = 100
    parents_n = pop_size/2
    #limit = 100
    
    #problem
    solution_size = 15
    gene_range = (-5,10)
    p_type = "MIN"
    
    #operator parameters
    sample_size = 5
    mutation_rate = 0.1
    step1 = 0.4
    step2 = 0.6
    step3 = 0.8
    step4 = 1
    
    #executions
    #n=1
    
    problem = Problem.FunctionProblem(name, solution_size, gene_range, p_type, function)
    
    a_crossover = C.ArithmeticCrossover()
    wa_crossover = C.WholeArithmeticCrossover()
    
    uf_mutation = M.UniformMutation(mutation_rate)
    nuf_mutation1 = M.NonuniformMutation(mutation_rate, step1)
    nuf_mutation2 = M.NonuniformMutation(mutation_rate, step2)
    nuf_mutation3 = M.NonuniformMutation(mutation_rate, step3)
    nuf_mutation4 = M.NonuniformMutation(mutation_rate, step4)
    
    
    tournament_parent = P.ParentTournamentSelection(sample_size)
    
    elitist_selection = G.ElitistSelection()
    
    #1 Elitismo
    title = name + ' | wa_crossover | Elitism'
    algs = []
    algs.append(GA("Uniform", problem, wa_crossover, uf_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step1), problem, wa_crossover, nuf_mutation1, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step2), problem, wa_crossover, nuf_mutation2, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step3), problem, wa_crossover, nuf_mutation3, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step4), problem, wa_crossover, nuf_mutation4, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))

    run(algs, n, title)
    
    #2 Elitismo
    title = name + ' | a_crossover | Elitism'
    algs = []
    algs.append(GA("Uniform", problem, a_crossover, uf_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step1), problem, a_crossover, nuf_mutation1, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step2), problem, a_crossover, nuf_mutation2, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step3), problem, a_crossover, nuf_mutation3, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    algs.append(GA("Nonuniform "+str(step4), problem, a_crossover, nuf_mutation4, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit))
    
    run(algs, n, title)
    
    
    
def run(algs, n, name):
    exps = []
    for alg in algs: 
        e = exp.Experiment(alg.name)
        e.run(alg,n)
        exps.append(e)
        
    plot.plot(exps, name)

#
pop_size = 100
limit = 50
n = 30

sphere = f.sphere
rastrigin = f.rastrigin
rosenbrock = f.rosenbrock
zakharov = f.zakharov

# sphere
name = "Sphere"
exp3(name, sphere, pop_size, limit, n)

name = "Rastrigin"
exp3(name, rastrigin, pop_size, limit, n)

name = "Rosenbrock"
exp3(name, rosenbrock, pop_size, limit, n)

name = "Zakharov"
exp3(name, zakharov, pop_size, limit, n)