import random

class Mutation(object):
    
    def __init__(self, p):
        self.p = p
    
    def mutation(self, c):
        raise NotImplementedError("Method hasn't been implemented.")

class RandomResettingMutation(Mutation):
    
    #TODO Use random generator from Problem class
    def mutation(self, c):
        for g in range(c.size()):
            if random.random() < p:
                