import numpy as np
class Main:
    def __init__(self, r1 ,r2):
        self.r1 = r1
        self.r2 = r2

    def K1 (self, threshhold=1):
        r_total = self.r1 + self.r2
        if (r_total) > threshhold:
            k1 = r_total
            return k1
        else:
            return 0
        
    def K2 (k1, threshhold=0.2):
        if k1 > threshhold:
            k2 = k1 + threshhold
            return k2
        else:
            return 0
        
    def P1 (k1, threshhold = 0.1):
        if k1 > threshhold:
            p1 = 1/(1+np.exp(k1-threshhold))
            return p1
        else:
            return 0
        
    def K3 (p1, threshhold=0.01):
        if p1 > threshhold:
            k3 = p1 - threshhold
            return k3
        else:
            return 0
        
    def C (k2, k3, threshhold=0.15):
        if min(k2,k3) > threshhold:
            c = min(k2,k3)
            return c
        else:
            return 0
        
    def A (c, threshhold = 0.1):
        if c > threshhold:
            return True
        else:
            return False
    
    def simulation(self):
        k1 = K1(self.r1, self.r2)
        p1 = P1(k1)
        k3 = K3(p1)
        k2 = K2(k1)
        c = C(k2,k3)
        Apotosis = A(c)
        print(Apotosis)
    
var = Main(0.3, 0.8)
var.simulation()