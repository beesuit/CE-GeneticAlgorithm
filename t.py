from scipy.optimize import rosen, differential_evolution
import pqm
import util

def get_wlnn():
    train_classes = [0,1]
    test_class=None
    train_X, train_y = util.load_dataset('SPECT.train', 1)
    
    divided_samples = {str(train_class): [] for train_class in train_classes}
    #print(divided_samples)
    
    for sample, label in zip(train_X, train_y):
        label = ''.join(map(str, label))
        divided_samples[label].append(sample)
        
    test_X, test_y = util.load_dataset('SPECT.test', 1)
    
    if test_class != None:
        test_class = [test_class]
        test_X = [sample[0] for sample in zip(test_X,test_y) if sample[1] == test_class]
        test_y = [test_class]*len(test_X)
    
    # setup pqms and wlnn
    c_bits = 1
    pqms = []
    for label in divided_samples.keys():
        #print(list(label))
        pqms.append(pqm.PQMClassifier(divided_samples[label], c_bits, [int(label)]))
    
    #print(pqms)
    wlnn = pqm.WLNN(pqms)
    
    return wlnn, test_X, test_y

def wlnn_test(params, *args):
    wlnn = args[0]
    test_X = args[1] 
    test_y = args[2] 
    
    hits = 0
    for i in range(len(test_X)):
        result = wlnn.classify(test_X[i], params)
        #print(result, test_y[i])
        
        if result == test_y[i]:
            hits += 1
    
    acc = hits/len(test_X)
    return 1-acc

def call(xk, convergence):
    print(xk, convergence)
    #pass

mutation = (1.5,1.9)
recombination = 1
args = get_wlnn()
#[0.87253771 0.84823509]
bounds = [(0.01, 1), (0.01, 1)]
result = differential_evolution(wlnn_test, bounds, args=args, disp=True, callback=call, popsize=50, mutation=mutation, recombination=recombination)
print(result.x, result.fun)
    


#def a(*args):
#    return args
#
#def t(*args):
#    v1 = args
#    print(v1)
#    v2 = a(2,3)
#    for i,j in zip(v1,v2):
#        print(i,j)
#
#t(0,1)
