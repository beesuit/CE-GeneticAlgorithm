import random
import numpy as np

class Constraint(object):
    
    def __init__(self):
        pass
        
    def constraint(self, c):
        raise NotImplementedError("The method hasn't been implemented yet.")

class Constraint_allZero(Constraint):
    
    def constraint(self, c, precision):
        
        param_n = c.size()//precision 
        
        for i in range(param_n):
            
            param = c.chromossome[i*precision:(i+1)*precision]
        
            if np.count_nonzero(param) == 0:
                
                position = random.randint(i*precision, (i+1)*precision-1)
                
                c.chromossome[position] = 1
                    