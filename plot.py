import matplotlib.pyplot as plt

def plot(exps, filename):
    plt.xlabel("Generations")
    plt.ylabel("Fitness");
    plt.title(filename)
    for exp in exps:
        plt.plot(exp.mean_results(), label=exp.name)
    
    plt.legend()
    plt.savefig(filename)
    
    plt.clf()