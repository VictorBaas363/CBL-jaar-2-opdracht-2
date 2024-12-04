import numpy as np

class Pathway:
    def __init__(self, thr):
        self.thr = thr

    def activation(self, x, y):
        if x > self.thr:
            return y
        else:
            return 0
        
    def Apoptosis(self, x):
        y = x
        if y > self.thr:
            return True
        else:
            return False

class Kinase(Pathway):       
    def kinase_1(self, x1, x2):
        x = x1 + x2
        y = x
        return self.activation(x, y)

    def kinase_2(self, x):
        y = x + self.thr
        return self.activation(x, y)


    def kinase_3(self, x,):
        y = x - self.thr
        return self.activation(x, y)

class Phosphatase(Pathway):
    def phosphatase(self, x):
        y = 1/(1 + np.exp(x - self.thr))
        return self.activation(x, y)


class Complex(Pathway):
    def complex(self, x1, x2):
        x = min(x1, x2)
        y = x
        return self.activation(x, y)


def simulation(r1, r2):
    kin_1 = Kinase(1.0)
    kin_2 = Kinase(0.2)
    kin_3 = Kinase(0.01)
    phos = Phosphatase(0.1)
    comp = Complex(0.15)
    apop = Pathway(0.1)

    kinase_1 = kin_1.kinase_1(r1, r2)
    kinase_2 = kin_2.kinase_2(kinase_1)
    phosphatse = phos.phosphatase(kinase_1)
    kinase_3 = kin_3.kinase_3(phosphatse)
    complex = comp.complex(kinase_2, kinase_3)
    apoptosis = apop.Apoptosis(complex)
    print(apoptosis)

simulation(0.3, 0.8)

