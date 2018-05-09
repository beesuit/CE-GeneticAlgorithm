import numpy as np

class Experiment(object):
    
    def __init__(self, name):
        self.name = name
        self.results = []
        
    def run(self, ga, n):
        self.results.clear()
        for i in range(n):
            result = ga.run()
            self.results.append(result)
        
        return self.results
    
    def mean_results(self):
        return np.mean(np.array(self.results), axis=0)