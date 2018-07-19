import numpy as np
import util

class PQM(object):
    
    def __init__(self, patterns):
        self.patterns = patterns
    
    def memory_retrieval(self, input_pattern, nvalue=1):
        i = input_pattern
        pi = np.pi
        p = len(self.patterns)
        n = len(input_pattern)
        
        amp = 1/p
        
        sum_value = 0
        for k in range(p):
            dh = util.hamming_distance(i, self.patterns[k])
            v = (pi/(2*n * nvalue))*dh
            
            sum_value += np.cos(v)**2
    
        return amp * sum_value
    
class PQMClassifier(PQM):
    
    def __init__(self, patterns, pqm_class):
        PQM.__init__(self, patterns)
        self.pqm_class = pqm_class
    
    def classify(self, pattern, nvalue):
        return self.memory_retrieval(pattern, nvalue)