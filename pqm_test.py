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
import math
import pickle
import os
import numpy as np

def wlnn_exp():
    #experiments = []
    
    #GA
    pop_size = 200
    parents_n = pop_size/2
    limit = 3
    
    #pqm
    solution_size = 15
    precision = solution_size
    gene_range = (0,1)
    p_type = "MAX"
    
    #operator
    sample_size = 2
    mutation_rate = 0.2
    
    #executions
    #n = 50
    n=2
    
    
    train_X, train_y = util.load_dataset('SPECT.train', 1)
    #setup train dataset
    train_classes = [0,1]
    divided_samples = {str(train_class): [] for train_class in train_classes}
    #print(divided_samples)
    
    for sample, label in zip(train_X, train_y):
        label = ''.join(map(str, label))
        divided_samples[label].append(sample)
    
    # setup pqms and wlnn
    c_bits = 1
    pqms = []
    for label in divided_samples.keys():
        #print(list(label))
        pqms.append(pqm.PQMClassifier(divided_samples[label], c_bits, [int(label)]))
    
    #print(pqms)
    wlnn_classifier = pqm.WLNN(pqms)
    
    test_X, test_y = util.load_dataset('SPECT.test', 1)
    
    #problem = Problem.PQMProblem('pqm', solution_size, precision, gene_range, p_type, pqm_classifier, test_X, test_y)
    
    problem = Problem.WLNNProblem('wlnn', solution_size, precision, gene_range, p_type, wlnn_classifier, test_X, test_y)
    
    point_crossover = C.OnePointCrossover()
    uniform_crossover = C.UniformCrossover(p=0.5)
    
    #random_point_mutation = M.RandomPointMutation(mutation_rate)
    resetting_mutation = M.RandomResettingMutation(mutation_rate)
    swap_mutation = M.SwapMutation(mutation_rate)
    
    tournament_parent = P.ParentTournamentSelection(sample_size)
    uniform_parent = P.ParentUniformSelection(0.2)
    
    elitist_selection = G.ElitistSelection(maximize=True)
    robin_selection = G.RoundRobinSelection(sample_size, maximize=True)
    
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
    
    #SAVE
    name = 'First'
    save(name, exps)
    
    #LOAD and PLOT
    obj = load(name)
    plot.plot(obj, name)
    
def save(name, obj):
    with open(name+".p", "wb" ) as file:
        pickle.dump(obj, file)

def load(name):
    with open(name+".p", "rb" ) as file:
        solutions = pickle.load(file)
    
    return solutions

if __name__ == '__main__':
    wlnn_exp()
    