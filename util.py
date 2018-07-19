import csv

def load_dataset(name, label_size):
    folder = 'dataset/'
    
    with open(folder+name) as file:
        X = []
        y = []
        for row in csv.reader(file):
            X.append([int(row[i]) for i in range(len(row)-label_size)])
            y.append([int(row[i]) for i in range(len(row)-label_size, len(row))])
        
        return X, y

# Computes the Hamming distance
def hamming_distance(u, v):
    diff_n = 0
    
    for value1, value2 in zip(u, v):
        if value1 != value2:
            diff_n += 1
    
    return diff_n