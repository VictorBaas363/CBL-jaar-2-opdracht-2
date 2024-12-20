import numpy as np

class Pathway:
    '''A parent class that defines the threshhold, activation and apotosis'''
    def __init__(self, thr):
        self.thr = thr

    def activation(self, x, y):
        '''x is the input of a element in the pathway, y is the output'''
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
    '''A class containing the kinases'''     
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
    '''A class for the phosphatase'''
    def phosphatase(self, x):
        y = 1/(1 + np.exp(x - self.thr))
        return self.activation(x, y)


class Complex(Pathway):
    '''A class for'''
    def complex(self, x1, x2):
        x = min(x1, x2)
        y = x
        return self.activation(x, y)


def simulation(r1, r2):
    '''A function used to simulate the pathway, first makes the objects and then use functions on the objects. Returns apotosis (True or False)'''
    kin_1 = Kinase(1.0)
    kin_2 = Kinase(0.2)
    kin_3 = Kinase(0.01)
    phos = Phosphatase(0.1)
    comp = Complex(0.15)
    apop = Pathway(0.1)

    kinase_1 = kin_1.kinase_1(r1, r2)
    kinase_2 = kin_2.kinase_2(kinase_1)
    phosphatase = phos.phosphatase(kinase_1)
    kinase_3 = kin_3.kinase_3(phosphatase)
    complex = comp.complex(kinase_2, kinase_3)
    apoptosis = apop.Apoptosis(complex)
    print(apoptosis)
    return apoptosis

simulation(0.3, 0.8)

