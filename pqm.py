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

if __name__ == '__main__':

    patterns = [[1,1,1]]
    patterns = [[0,1,1,1], [1,1,1,1]]
    pqm = PQMClassifier(patterns, 'a')
    
    n = 1
    result = pqm.classify([0,0,0,0], n)
    
    print(result)
    print(75/1024)
    print(int(3.2))
    print(int(3.2))
    
    def decimal_input(input_value, memory_size):
        pattern = np.binary_repr(input_value, memory_size)
        return pattern
    
    def load_data(patterns, memory_size):
        amplitudes = np.zeros([memory_size**2])
        for value in patterns:
            amplitudes[int(value, 2)] = 1
        amplitudes = amplitudes / np.linalg.norm(amplitudes)
        return amplitudes
    
    test = decimal_input(2, 2)
    print(test)
    
    p = ['1010']
    print(int(p[0],2))
    
    amp = load_data(p, 4)
    print(amp)