import numpy as np

class Pathway:
    def __init__(self, thr):
        self.thr = thr

    def activation(self, y):
        if y > self.thr:
            return y
        else:
            return 0

class Kinase(Pathway):       
    def kinase_1(self, x1, x2):
        y = x1 + x2
        return self.activation(y)

    def kinase_2(self, x):
        y = x + self.thr
        return self.activation(y)


    def kinase_3(self, x,):
        y = x - self.thr
        return self.activation(y)

class Phosphatase(Pathway):
    def phosphatase(self, x):
        y = 1/(1 + np.exp(x - self.thr))
        return self.activation(y)


class Complex(Pathway):
    def complex(self, x1, x2):
        y = min(x1, x2)
        return self.activation(y)

def Apoptosis(y, thr = 0.1):
    if y > thr:
        return True
    else:
        return False

def simulation(r1, r2):
    kinase_1 = Kinase(1.0).kinase_1(r1, r2)
    kinase_2 = Kinase(0.2).kinase_2(kinase_1)
    phosphatse = Phosphatase(0.1).phosphatase(kinase_1)
    kinase_3 = Kinase(0.01).kinase_3(phosphatse)
    complex = Complex(0.15).complex(kinase_2, kinase_3)
    print(Apoptosis(complex))

