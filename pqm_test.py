import Problem
import Crossover_op as C
import Mutation_op as M
import ParentSelection_op as P
import GenerationSelection_op as G
import Experiment as exp
import plot
from GA import GA
import util
import pqm
import Constraint_op as Cons

def pqm_class(param):
    train_X, train_y = util.load_dataset('SPECT.train', 1)
    pqm_class = [0]
    
    train_X0 = [sample[0] for sample in zip(train_X,train_y) if sample[1] == pqm_class]
    
    test_X, test_y = util.load_dataset('SPECT.test', 1)
    
    pqm_classifier = pqm.PQMClassifier(train_X0, pqm_class)
    
    error = 0
    for i in range(len(test_X)):
        result = pqm_classifier.classify(test_X[i], param)
        
        if test_y[i] == pqm_classifier.pqm_class:
            error += (1 - result)**2
        else:
            error += result**2
    
    print(error/len(test_X))

def pqm_exp():
    #experiments = []
    
    #GA
    pop_size = 100
    parents_n = pop_size/2
    limit = 30
    
    #pqm
    solution_size = 200
    precision = solution_size-1
    gene_range = (0,1)
    p_type = "MIN"
    
    #operator
    sample_size = 5
    mutation_rate = 0.1
    
    #executions
    #n = 50
    n=1
    
    #setup pqm classifier
    train_X, train_y = util.load_dataset('SPECT.train', 1)
    pqm_class = [0]
    
    train_X0 = [sample[0] for sample in zip(train_X,train_y) if sample[1] == pqm_class]
    
    test_X, test_y = util.load_dataset('SPECT.test', 1)
    
    pqm_classifier = pqm.PQMClassifier(train_X0, pqm_class)
    
    problem = Problem.PQMProblem('pqm', solution_size, precision, gene_range, p_type, pqm_classifier, test_X, test_y)
    
    point_crossover = C.OnePointCrossover()
    uniform_crossover = C.UniformCrossover(p=0.5)
    
    #random_point_mutation = M.RandomPointMutation(mutation_rate)
    resetting_mutation = M.RandomResettingMutation(mutation_rate)
    swap_mutation = M.SwapMutation(mutation_rate)
    
    tournament_parent = P.ParentTournamentSelection(sample_size)
    uniform_parent = P.ParentUniformSelection(0.2)
    
    elitist_selection = G.ElitistSelection()
    robin_selection = G.RoundRobinSelection(sample_size)
    
    #constraint
    cons = Cons.Constraint_allZero()
    
    #1
    algs = []
    algs.append(GA("Variação alta", problem, uniform_crossover, resetting_mutation, uniform_parent, robin_selection, pop_size=pop_size, parents_n=parents_n, limit=limit, constraint=cons))
    algs.append(GA("Pressão evolutiva alta", problem, point_crossover, swap_mutation, tournament_parent, elitist_selection, pop_size=pop_size, parents_n=parents_n, limit=limit, constraint=cons))
    
    exps = []
    for alg in algs: 
        e = exp.Experiment(alg.name)
        e.run(alg,n)
        exps.append(e)
    
    plot.plot(exps, 'Extremos')

if __name__ == '__main__':
    #pqm_exp()
    param = 0.90120
    param2 = 0.90029
    param3 = 0.90029515745119333168095970479165924594311356191920307568205
    #param2 = 
    pqm_class(param3)
#    0.23855880806830695
#    0.23855880806830695
#    
#    0.23855843631203175
#    0.23855843631203175