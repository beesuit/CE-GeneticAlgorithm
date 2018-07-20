import random
import numpy as np

class Constraint(object):
    
    def __init__(self):
        pass
        
    def constraint(self, c):
        raise NotImplementedError("The method hasn't been implemented yet.")

class Constraint_allZero(Constraint):
    
    def constraint(self, c):
        
        if np.count_nonzero(c) == 0:
            point = random.randint(0, c.size()-1)
            c.chromossome[point] = 1
                