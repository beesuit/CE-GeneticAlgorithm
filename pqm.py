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

patterns = [[1,1,1], [0,1,0]]
pqm = PQMClassifier(patterns, 'a')
n = 1
result = pqm.classify([0,0,0], n)
print(result)

a=0.7
print(1/a)

def best2(f1, f2, p_type):
    if f1 < f2:
        if p_type == 'MIN':
            return True
        else:
            return False
    elif p_type == 'MAX':
        return True
    else:
        return False

def best(f1, f2, p_type):
    compare = f1 < f2
    
    if p_type == 'MIN':
        return compare
    elif p_type == 'MAX':
        return not compare

f1 = 0.5
f2 = 0.6

print(best(f1, f1, 'MIN'))