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
