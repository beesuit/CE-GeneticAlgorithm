import numpy as np
import util
from scipy.special import binom

class PQM(object):
    
    def __init__(self, patterns, control_bits_n):
        self.patterns = patterns
        self.control_bits_n = control_bits_n
    
    def memory_retrieval(self, input_pattern, nvalue):
        i = input_pattern
        pi = np.pi
        b = self.control_bits_n
        p = len(self.patterns)
        n = len(input_pattern)
        
        #Probabilities array
        p_array = []
        
        #For each number of 1 bits
        for l in range(b+1):
            amp = binom(b, l) * (1/p)
            sum_value = 0
            for k in range(p):
                dh = util.hamming_distance(i, self.patterns[k])
                v = (pi/(2*n * nvalue))*dh
                
                sum_value += (np.cos(v)**(2*b-2*l)) * (np.sin(v)**(2*l))
                
            p_array.append(amp * sum_value)
        
        #TODO CHECK exp value
        s = self.__expected_value(p_array)
        
        return s
    
    def __expected_value(self, p_array):
        s = 0
        for i in range(len(p_array)):
            s += i*p_array[i]
        
        return s

class PQMClassifier(PQM):
    
    def __init__(self, patterns, control_bits_n, label):
        PQM.__init__(self, patterns, control_bits_n)
        self.label = label
    
    def classify(self, pattern, nvalue):
        return self.memory_retrieval(pattern, nvalue)

class WLNN(object):
    
    def __init__(self, classifiers):
        self.classifiers = classifiers
        self.neurons_n = len(self.classifiers)
    
    def classify(self, pattern, params):
        #TODO CHECK otimization
        best_result = float('inf')
        best_class = None
        
        for classifier, param in zip(self.classifiers, params):
            result = classifier.classify(pattern, param)
            
            if result < best_result:
                best_result = result
                best_class = classifier.label
        
        return best_class
        
if __name__ == '__main__':

#    patterns = [[1,1,1]]
#    patterns = [[0,1,1,1], [1,1,1,1]]
#    pqm = PQMClassifier(patterns, 'a')
#    pqm2 = PQMClassifier(patterns, 'b')
#    w = WLNN(pqm, pqm2)
    
    train_classes = [0,1]
    divided_samples = {str(train_class): [] for train_class in train_classes}
    
    print(divided_samples)
#    n = 1
#    result = pqm.classify([0,0,0,0], n)
#    
#    print(result)
#    print(75/1024)
#    print(int(3.2))
#    print(int(3.2))
#    
#    def decimal_input(input_value, memory_size):
#        pattern = np.binary_repr(input_value, memory_size)
#        return pattern
#    
#    def load_data(patterns, memory_size):
#        amplitudes = np.zeros([memory_size**2])
#        for value in patterns:
#            amplitudes[int(value, 2)] = 1
#        amplitudes = amplitudes / np.linalg.norm(amplitudes)
#        return amplitudes
#    
#    test = decimal_input(2, 2)
#    print(test)
#    
#    p = ['1010']
#    print(int(p[0],2))
#    
#    amp = load_data(p, 4)
#    print(amp)