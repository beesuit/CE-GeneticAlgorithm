import math

def sphere(values):
    s = 0
    for x in values:
        s += x*x
        
    return s

def rastrigin(values):
    d = len(values)
    s = 0
    for x in values:
        s += (x**2) - 10*math.cos(2*math.pi*x)
        
    return 10*d + s

def rosenbrock(values):
    s = 0
    for i in range(len(values)-1):
        s += 100*(values[i+1]-values[i]**2)**2 + (values[i]-1)**2
    
    return s

def zakharov(values):
    s1 = 0
    s2 = 0
    for i in range(len(values)):
        x = values[i]
        s1 += x*x
        s2 += 0.5*i*x
    
    return s1 + s2**2 + s2**4
    