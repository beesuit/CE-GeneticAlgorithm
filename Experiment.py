import numpy as np

class Experiment(object):
    
    def __init__(self, name):
        self.name = name
        self.results = []
        self.best_solution = None
        
    def run(self, ga, n):
        self.results.clear()
        for i in range(n):
            print('Execution',i)
            result = ga.run()
            self.results.append(result)
            
            best = ga.best_solution
            if self.best_solution != None:
                if ga.problem.best(best.fitness, self.best_solution['fitness']):
                    self.best_solution = {'params':ga.problem.decode_solution(best.chromossome), 'fitness': best.fitness}
            else:
                self.best_solution = {'params':ga.problem.decode_solution(best.chromossome), 'fitness': best.fitness}
            
        
        return self.results
    
    def mean_results(self):
        return np.mean(np.array(self.results), axis=0)