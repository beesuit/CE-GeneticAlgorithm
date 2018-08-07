import csv
import numpy as np
import pandas

def load_dataset(name, label_size):
    folder = 'dataset/'
    
    with open(folder+name) as file:
        X = []
        y = []
        for row in csv.reader(file):
            X.append([int(row[i]) for i in range(len(row)-label_size)])
            y.append([int(row[i]) for i in range(len(row)-label_size, len(row))])
        
        return X, y
    
def read_pandas_dataset(file):
    ext = '.csv'
    folder = 'dataset/'
    filepath = folder + file + ext
    data = pandas.read_csv(filepath, converters={'Hits':eval})
    return data
    
def get_arcs(file, arcs):
    data = read_pandas_dataset(file)
    # Mean performances array
    mean_perfs = []
    hit_vectors = []
    
    # For every architecture calculate quantum equation probabilities
    for arc in arcs:
        # Filter data by architecture
        arc_filter = data.Architecture == arc
        
        # Get Hits vectors
        hits = data[arc_filter].Hits.values
        
        # Get Performances mean and add to dict
        perf_mean = data[arc_filter].Performance.mean()
        
        hit_vectors.append(list(hits))
        mean_perfs.append(perf_mean)
        
    return list(hit_vectors), list(mean_perfs)
    

# Computes the Hamming distance
def hamming_distance(u, v):
    diff_n = 0
    
    for value1, value2 in zip(u, v):
        if value1 != value2:
            diff_n += 1
    
    return diff_n

if __name__ == '__main__':
    
    file = 'cancer'
    
    
    h,p = get_arcs(file, [5,20])
    print(h)
    print(p)

#    a = np.binary_repr(999)
#    
#    print(a)
#    
#    
#    f = 1.00
#    int32bits = np.asarray(f, dtype=np.float32).view(np.int32).item()
#    print('{:032b}'.format(int32bits))
#    print(bin(int32bits))
#    
#    precision = 5
#    
#    a = '1111111111111111111111111'
#    #b = np.binary_repr(a)
#    b = int(a,2)
#    print(b)
#    #print(b/100000)
#    print(b/10**len(str(b)))
#    
#    bb = [0,1,0]
#    bb = ''.join(map(str, bb))
#    #bb = ''.join(bb)
#    print(bb)
#    print(int(bb,2))
#    
#    print(np.count_nonzero([1,1,1]))
#    
#    train_X, train_y = load_dataset('SPECT.train',1)
#    
#    train_X0 = [sample[0] for sample in zip(train_X,train_y) if sample[1] == [0]]
#    print(len(train_X0))
#    
#    tes = []
#    for i in range(len(train_y)):
#        if train_y[i] == [0]:
#            tes.append(train_X[i])
#    print(len(tes))
#    print(str(train_X0) == str(tes))
#    
#    #v1 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#    v1 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
#    v2 = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
#    #v1 = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
#    #v2 = [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
#    v1 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1] 
#    v2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
#    
#    print(int(''.join(map(str, v1)),2), 'value1')
#    print(int(''.join(map(str, v2)),2), 'value2')
    
    
    