import csv

def load_dataset(name):
    folder = 'dataset/'
    with open(folder+name) as file:
        return [[int(value) for value in row] for row in csv.reader(file)]